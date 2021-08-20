class Solution:

    def maxUniqueSplit(self, S: str) -> int:
        n = len(S)
        ans = 0
        for U in range(1 << n - 1):
            word = []
            now = S[0]
            for j in range(n - 1):
                if U >> j & 1:
                    word.append(now)
                    now = S[j + 1]
                else:
                    now += S[j + 1]
            word.append(now)
            if len(word) == len(set(word)):
                ans = max(ans, len(word))
        return ans
