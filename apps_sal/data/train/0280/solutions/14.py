class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        self.memo = {}
        return self.dfs(s, k)
    
    def dfs(self, s, k):
        if (s, k) not in self.memo:
            res = float('inf')
            if len(s) == k:
                res = 0
            elif k == 1:
                res = sum(s[i] != s[-1-i] for i in range(len(s)//2))
            else:
                for i in range(1, len(s) - k + 2):
                    res = min(self.dfs(s[:i], 1) + self.dfs(s[i:], k - 1), res)
            self.memo[s, k] = res
        return self.memo[s, k]

