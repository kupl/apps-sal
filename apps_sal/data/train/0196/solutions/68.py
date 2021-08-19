class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        greatest: int = -sys.maxsize + 1
        smallest: int = sys.maxsize
        x = y = total = 0
        for i in range(len(nums)):
            x += nums[i]
            greatest = max(greatest, x)
            x = max(x, 0)
            y += nums[i]
            smallest = min(smallest, y)
            y = min(y, 0)
            total += nums[i]
        return greatest if greatest < 0 else max(greatest, total - smallest)
