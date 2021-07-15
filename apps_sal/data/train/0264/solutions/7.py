class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        def dfs(n, s, l, cur):
            nonlocal res
            if n == l:
                if len(set(cur)) == len(cur):
                    res = max(res, len(cur))
                return
            for i in range(s, len(arr)):
                new_cur = cur + arr[i]
                if len(set(cur)) != len(cur):
                    return
                dfs(n, i+1, l+1, new_cur)
        for i in range(len(arr)+1):
            dfs(i, 0, 0, '')
        return res

