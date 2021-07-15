class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        arr = list([x for x in arr if len(set(x))==len(x)])
        arr = [set(x) for x in arr]
        def dfs(n, s, l, cur):
            nonlocal res
            if n == l:
                res = max(res, len(cur))
                return
            for i in range(s, len(arr)):
                if len(cur.intersection(arr[i])) == 0:
                    dfs(n, i+1, l+1, cur.union(arr[i]))
                # new_cur = cur + arr[i]
                # if len(set(new_cur)) != len(new_cur):
                #     return
                # dfs(n, i+1, l+1, new_cur)
        for i in range(len(arr)+1):
            dfs(i, 0, 0, set())
        return res

