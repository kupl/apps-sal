from collections import Counter
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = [1] * len(words)
        words.sort(key=len)
        for i in range(1, len(words)):
            d1 = Counter(words[i])
            for j in range(i):
                if len(words[i]) - len(words[j]) == 1:
                    d2 = Counter(words[j])
                    check = 0
                    for k in d1:
                        if k not in d2:
                            check += 1
                        elif d2[k] != d1[k]:
                            check += 1
                        if check == 2:
                            break
                    if check == 1:
                        dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
