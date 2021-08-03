class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        n = len(arr)
        if m == n:
            print(n)

        def dfs(start: int, end: int, step: int, target: int):
            if end > len(arr) or end < 1:
                return -1
            if start > len(arr) or start < 1:
                return -1
            if end < start:
                return -1
            if end - start + 1 < target:
                return -1

            if end - start + 1 == target:
                return step
            bp = arr[step - 1]
            res = -1
            if start <= bp <= end:
                res = max(dfs(start, bp - 1, step - 1, target),
                          dfs(bp + 1, end, step - 1, target))
            else:
                res = max(res, dfs(start, end, step - 1, target))
            return res

        return dfs(1, n, n, m)
