from collections import Counter


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c = Counter(s[:k])
        m = sum([c[x] for x in 'aeiou'])
        for i in range(len(s) - k):
            c[s[i]] -= 1
            c[s[i + k]] += 1
            m = max(m, sum([c[x] for x in 'aeiou']))
        return m
