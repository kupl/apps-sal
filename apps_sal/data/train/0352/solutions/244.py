class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def f(x, y):
            if len(x) != len(y) - 1:
                return False
            p = len(x)
            for i in range(len(x)):
                if x[i] != y[i]:
                    p = i
                    break
            for i in range(p, len(x)):
                if x[i] != y[i + 1]:
                    return False
            return True
        words.sort(key=lambda x: len(x))
        a = []
        for _ in range(len(words)):
            a.append([False] * len(words))
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                a[i][j] = f(words[i], words[j])
        dp = [1] * len(words)
        for i in range(1, len(words)):
            for j in range(i):
                if a[j][i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
