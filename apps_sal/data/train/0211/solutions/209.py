class Solution:

    def maxUniqueSplit(self, s: str) -> int:

        def backtrack(m, s):
            if len(s) == 0:
                return 0
            ans = 0
            for i in range(1, len(s) + 1):
                candidate = s[:i]
                if candidate not in m:
                    m.add(candidate)
                    ans = max(ans, 1 + backtrack(m, s[i:]))
                    m.remove(candidate)
            return ans
        m = set()
        return backtrack(m, s)
