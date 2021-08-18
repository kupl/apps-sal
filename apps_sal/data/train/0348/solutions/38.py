class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if max(arr) < 0:
            return max(arr)

        @lru_cache(maxsize=None)
        def recurse(idx, isSkipped):
            if idx == len(arr):
                return 0

            if isSkipped:
                return max(arr[idx] + recurse(idx + 1, True), 0)
            else:
                return max(arr[idx] + recurse(idx + 1, False), recurse(idx + 1, True), arr[idx])

        curMax = float('-inf')
        for i in range(len(arr)):
            curMax = max(recurse(i, False), curMax)

        return curMax
