class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPredecessor(a, b):
            if len(a) != len(b) -1 or len(b) == 1:
                return False
            for i in range(len(b)):
                tmp = b[:i] + b[i+1:]
                if a == tmp:
                    return True
            return False
        words.sort(key=len)
        dp = [1] * (len(words))
        for i in range(len(dp)):
            for j in range(i-1, -1, -1):
                if isPredecessor(words[j], words[i]):
                    dp[i] = max(dp[j] +1, dp[i])
        return max(dp)
