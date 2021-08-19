def chain(w1, w2):
    (m, n) = (len(w1), len(w2))
    if abs(m - n) != 1:
        return False
    (i, j, one) = (0, 0, 1)
    while i < m and j < n:
        if w1[i] == w2[j]:
            (i, j) = (i + 1, j + 1)
        elif one:
            (one, i) = (0, i + 1)
        else:
            return False
    return True


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dp = [1] * len(words)
        dp[0] = 1
        words.sort(key=lambda x: len(x))
        for i in range(1, len(words)):
            for j in range(0, i):
                if chain(words[i], words[j]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
