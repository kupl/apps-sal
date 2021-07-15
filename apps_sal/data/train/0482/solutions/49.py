class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @lru_cache(maxsize=None)
        def helper(start, end):
            if start >= end:
                return 0
            
            result = float('inf')
            for i in range(start, end):
                rootVal = max(arr[start:i + 1]) * max(arr[i + 1:end + 1])
                result = min(result, rootVal + helper(start, i) + helper(i + 1, end))
            return result
        return helper(0, len(arr) - 1)
