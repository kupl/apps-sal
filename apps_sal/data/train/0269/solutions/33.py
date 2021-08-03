class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # find the first 1:
        start = 0

        for ind in range(len(nums)):
            if nums[ind] == 1:
                start = ind
                break
        # return true if no 1's in the array, or there's only one 1 in the last place
        if start >= len(nums) - 1:
            return True

        minDist = float('inf')  # represents infinity
        print(start)

        # check rest of the array:
        for i in range(start + 1, len(nums)):
            if nums[i] == 1:
                dist = i - start - 1
                if dist < minDist:
                    minDist = dist
                start = i
        return minDist >= k

    # make faster:
    # enumerate(nums)
    # nums.index(1) --> gets index of first 1 apparently
