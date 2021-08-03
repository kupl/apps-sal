class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0

        def dfs(before_res, cur_s):
            nonlocal res
            if len(cur_s) == 0:
                res = max(res, len(before_res))
            for i in range(len(cur_s)):
                if cur_s[:i + 1] not in before_res:
                    before_res.add(cur_s[:i + 1])
                    dfs(before_res, cur_s[i + 1:])
                    before_res.remove(cur_s[:i + 1])

        dfs(set(), s)
        return res
