class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        if len(s) == 1:
            return 1
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = [set()]
        for end in range(1, n + 1):
            ls = []
            sub = set()
            for start in range(end):
                for ele in dp[start]:
                    last = ele.copy()
                    node = s[start:end]
                    last.add(node)
                    ls.append(last)
            dp[end] = ls
        res = 0
        for i in dp[-1]:
            if len(i) > res:
                res = len(i)
        return res
