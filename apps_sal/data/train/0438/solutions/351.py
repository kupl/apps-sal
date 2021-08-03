class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        def dfs(start, end, cur):
            if end - start + 1 < m:
                return -2
            if end - start + 1 == m:
                return cur
            while arr[cur] < start or arr[cur] > end:
                cur -= 1
            return max(dfs(start, arr[cur] - 1, cur - 1), dfs(arr[cur] + 1, end, cur - 1))
        return dfs(1, len(arr), len(arr) - 1) + 1
