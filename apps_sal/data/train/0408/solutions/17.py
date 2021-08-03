class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        low = 0
        high = max(arr)
        while low < high:
            mid = low + (high - low) // 2
            if self.sol(mid, arr, target) <= self.sol(mid + 1, arr, target):
                high = mid
            else:
                low = mid + 1
        return low

    def sol(self, n, num, target):
        result = 0
        for i in num:
            if i > n:
                result += n
            else:
                result += i
        return abs(result - target)
