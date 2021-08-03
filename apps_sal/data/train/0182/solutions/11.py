class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # find valleys
        N = len(height)
        valleys = []  # a list of [left, right] (not inclusive) bounds of local minimum
        i = 0
        while i < N - 1:
            # first go uphills and then down hills until flat or up hills, this is a potential left bound of a valley
            while i < N - 1 and height[i] <= height[i + 1]:
                i += 1
            while i < N - 1 and height[i] > height[i + 1]:
                i += 1  # ensures height[i] <= height[i+1] unless out of bounds
            j = i
            while j < N - 1 and height[j] == height[j + 1]:
                j += 1  # go through the range of the potential bottom of the valley
            if j < N - 1 and height[j] < height[j + 1]:
                valleys.append([i - 1, j + 1])  # store a confirmed valley with bottom [i:j+1]
            i = j

        # fill water into each valley
        total_water = 0
        further_valleys = []  # list of potential valley to merge as those whose left side is higher after water filll
        k = 0
        if valleys:  # initialize
            l = valleys[k][0]
            r = valleys[k][1]
            old_level = height[l + 1]
        while k < len(valleys):
            # record bottom level
            water = 0
            while l >= 0 and r < N and height[l] >= height[l + 1] and height[r - 1] <= height[r]:  # both sides rising
                # fill water at [l+1:r]
                new_level = min(height[l], height[r])
                water += (new_level - old_level) * (r - l - 1)
                old_level = new_level
                # advance to the next level in the valley
                if l >= 0 and r < N:
                    # rise only the lower side
                    if height[l] == height[r]:
                        l -= 1
                        r += 1
                    elif height[l] < height[r]:
                        l -= 1
                    else:
                        r += 1
                    # make sure level rises
                    while l >= 0 and height[l] == height[l + 1]:
                        l -= 1
                    while r < N and height[r - 1] == height[r]:
                        r += 1
            total_water += water

            # l == -1 or r == N or height[l] < height[l+1] or height[r-1] > height[r]
            if l >= 0 and r < N:
                if height[l] > height[l + 1]:  # further rise is possible after the next valley is filled
                    further_valleys.append([l, r])
                elif further_valleys and height[further_valleys[-1][1] - 1] == height[l + 1]:  # merge two valleys
                    old_level = height[l + 1]  # water already filled to this level
                    l = further_valleys[-1][0]
                    further_valleys.pop()
                    continue  # fill the merged valley before moving on

            # fill the next valley
            k += 1
            if k < len(valleys):
                l = valleys[k][0]
                r = valleys[k][1]
                old_level = height[l + 1]

        return total_water
