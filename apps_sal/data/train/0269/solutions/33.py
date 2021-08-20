class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        start = 0
        for ind in range(len(nums)):
            if nums[ind] == 1:
                start = ind
                break
        if start >= len(nums) - 1:
            return True
        minDist = float('inf')
        print(start)
        for i in range(start + 1, len(nums)):
            if nums[i] == 1:
                dist = i - start - 1
                if dist < minDist:
                    minDist = dist
                start = i
        return minDist >= k
