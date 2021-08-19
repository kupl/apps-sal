from collections import Counter


class Solution:

    def longestStrChain(self, words: List[str]) -> int:

        def in_c(a: int, b: int):
            for (k, v) in list(a.items()):
                if k not in b or b[k] < v:
                    return False
            return True
        N = len(words)
        words = sorted(words, key=lambda i: len(i))
        word_c = [Counter(ii) for ii in words]
        dp = [1] * N
        for ii in range(N):
            can = [kk for (jj, kk, mm) in zip(word_c[:ii], dp[:ii], words[:ii]) if len(words[ii]) == len(mm) + 1 and in_c(jj, word_c[ii])]
            if can:
                dp[ii] = max(can) + 1
        print(words)
        print(dp)
        return max(dp)
