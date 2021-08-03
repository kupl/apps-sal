from collections import Counter


class Solution:
    def is_one_away(self, str_1, str_2):
        c1 = Counter(str_1)
        c2 = Counter(str_2)
        diff = 0
        for k, v in c2.items():
            diff += v - c1.get(k, 0)
            if diff > 1:
                return False

        for k in c1:
            if k not in c2:
                return False

        return True

    def longestStrChain(self, words: List[str]) -> int:
        sorted_words = sorted([''.join(sorted(w)) for w in words], key=lambda x: len(x))
        dp = [1] * len(words)

        for i in range(len(sorted_words) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if len(sorted_words[i]) - len(sorted_words[j]) == 0:
                    continue

                if len(sorted_words[i]) - len(sorted_words[j]) > 1:
                    break

                if self.is_one_away(sorted_words[j], sorted_words[i]):
                    dp[j] = max(1 + dp[i], dp[j])

        return max(dp)
