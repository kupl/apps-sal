from collections import Counter


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        dp = [1]
        res = 0
        words = sorted(words, key=lambda x: len(x))
        for i in range(1, len(words)):
            j = i - 1
            val = 1
            while j >= 0:
                if len(words[j]) != len(words[i]) - 1:
                    j -= 1
                    continue
                (counter_j, counter_i) = (Counter(words[j]), Counter(words[i]))
                used = False
                for (key, value_j) in counter_j.items():
                    value_i = counter_i.get(key)
                    if not value_i or value_i > value_j + 1 or value_i < value_j:
                        break
                    if value_i == value_j + 1 and used:
                        break
                    if value_i == value_j + 1 and (not used):
                        used = True
                else:
                    val = max(val, dp[j] + 1)
                j -= 1
            dp.append(val)
            res = max(val, res)
        print(dp)
        return res
