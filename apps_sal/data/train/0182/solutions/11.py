class Solution:

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N = len(height)
        valleys = []
        i = 0
        while i < N - 1:
            while i < N - 1 and height[i] <= height[i + 1]:
                i += 1
            while i < N - 1 and height[i] > height[i + 1]:
                i += 1
            j = i
            while j < N - 1 and height[j] == height[j + 1]:
                j += 1
            if j < N - 1 and height[j] < height[j + 1]:
                valleys.append([i - 1, j + 1])
            i = j
        total_water = 0
        further_valleys = []
        k = 0
        if valleys:
            l = valleys[k][0]
            r = valleys[k][1]
            old_level = height[l + 1]
        while k < len(valleys):
            water = 0
            while l >= 0 and r < N and (height[l] >= height[l + 1]) and (height[r - 1] <= height[r]):
                new_level = min(height[l], height[r])
                water += (new_level - old_level) * (r - l - 1)
                old_level = new_level
                if l >= 0 and r < N:
                    if height[l] == height[r]:
                        l -= 1
                        r += 1
                    elif height[l] < height[r]:
                        l -= 1
                    else:
                        r += 1
                    while l >= 0 and height[l] == height[l + 1]:
                        l -= 1
                    while r < N and height[r - 1] == height[r]:
                        r += 1
            total_water += water
            if l >= 0 and r < N:
                if height[l] > height[l + 1]:
                    further_valleys.append([l, r])
                elif further_valleys and height[further_valleys[-1][1] - 1] == height[l + 1]:
                    old_level = height[l + 1]
                    l = further_valleys[-1][0]
                    further_valleys.pop()
                    continue
            k += 1
            if k < len(valleys):
                l = valleys[k][0]
                r = valleys[k][1]
                old_level = height[l + 1]
        return total_water
