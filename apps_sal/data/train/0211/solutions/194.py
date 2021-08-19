class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        d = set()
        res = 1
        n = len(s)

        def solve(p, ans):
            nonlocal res
            if p == n:
                res = max(res, ans)
            for i in range(p, n):
                ss = ''.join(s[p:i + 1])
                if ss in d:
                    continue
                d.add(ss)
                solve(i + 1, ans + 1)
                d.remove(ss)
        solve(0, 0)
        return res
