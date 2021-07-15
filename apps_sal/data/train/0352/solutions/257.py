class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key = len)
        n = len(words)
        def match(l, r):
            a = words[l]
            b = words[r]
            if (len(a) + 1 != len(b)):
                return False
            i,j = 0,0
            while i < len(a) and j < len(b):
                if (a[i] == b[j]):
                    i += 1
                j += 1
            return i == len(a)
        
        dp = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if (len(words[j]) > len(words[i])+1):
                    break
                if match(i, j):
                    dp[i] = max(dp[i], 1 + dp[j])
        return 1+max(dp)
