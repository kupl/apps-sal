class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def solve(S, subs):
            if not S:
                return len(subs)

            ans = 0
            for i in range(len(S)):
                sub = S[:i + 1]
                ans = max(ans, solve(S[i + 1:], subs | {sub}))

            return ans
        return solve(s, set())
