class Solution:

    def palindromePartition(self, s: str, k: int) -> int:
        self.cache = {}
        return self.dfs(s, k)

    def dfs(self, s, k):
        if (s, k) in self.cache:
            return self.cache[s, k]
        if k == 1:
            self.cache[s, k] = self.helper(s)
            return self.cache[s, k]
        n = len(s)
        ans = 100
        for i in range(n - k + 1):
            temp = self.helper(s[:i + 1])
            ans = min(ans, temp + self.dfs(s[i + 1:], k - 1))
        self.cache[s, k] = ans
        return ans

    def helper(self, s):
        (l, r) = (0, len(s) - 1)
        count = 0
        while l < r:
            if s[l] != s[r]:
                count += 1
            l += 1
            r -= 1
        return count
