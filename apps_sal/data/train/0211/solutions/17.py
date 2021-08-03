class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        def dp(i, cur):
            nonlocal ans
            if len(cur) + n - i < ans:
                return
            if i >= n:
                ans = max(ans, len(cur))
            l = n - i
            for k in range(1, l + 1):
                if s[i:i + k] not in cur:
                    cur.append(s[i:i + k])
                    dp(i + k, cur)
                    cur.pop()
        ans, cur = 0, []
        dp(0, cur)
        return ans
