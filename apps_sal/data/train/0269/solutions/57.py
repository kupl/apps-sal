class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # find the first 1:
        start = 0
        while start < len(nums):
            if nums[start] == 0:
                start += 1
            else:
                break
        if start >= len(nums) - 1:
            return True  # return true if no 1's in the array, or there's only one 1 in the last place

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
