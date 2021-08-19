class Solution:

    def maxLength(self, arr: List[str]) -> int:
        if not arr:
            return 0

        def isUnique(s):
            return len(set(s)) == len(s)

        def dfs(arr, res, curr):
            yield curr
            for i in range(len(arr)):
                yield from dfs(arr[i + 1:], res, curr + arr[i])
        res = 0
        for st in dfs(arr, res, ''):
            if isUnique(st):
                res = max(res, len(st))
        return res
