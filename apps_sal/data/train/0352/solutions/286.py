class Solution:
    def one_off(self, a, b):
        if abs(len(a) - len(b)) != 1:
            return False
        one_off = False
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] != b[j]:
                if one_off:
                    return False
                one_off = True
                if len(a) > len(b):
                    j -= 1
                else:
                    i -= 1
            i += 1
            j += 1

        return True

    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        words.sort(key=lambda word: -len(word))
        dp = {}
        best = 1
        for i, word in enumerate(words):
            for other in words[i + 1:]:
                if len(word) - 1 > len(other):
                    break
                if self.one_off(word, other):
                    dp[other] = max(dp.get(other, 0), dp.get(word, 1) + 1)
                    best = max(best, dp[other])
        return best
