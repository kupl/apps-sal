class Solution:

    def maxLength(self, arr: List[str]) -> int:
        if not arr:
            return 0

        def isUnique(s):
            return len(set(s)) == len(s)

        def dfs(arr, res, curr):
            if isUnique(curr):
                res[0] = max(res[0], len(curr))
            for i in range(len(arr)):
                dfs(arr[i + 1:], res, curr + arr[i])
        res = [0]
        dfs(arr, res, '')
        return res[0]
