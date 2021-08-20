class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        digits = {c: i for (i, c) in enumerate('aeiou')}
        counters = [0]
        for c in s:
            if c in digits:
                counters.append(counters[-1] ^ 1 << digits[c])
            else:
                counters.append(counters[-1])
        for length in range(len(s), 0, -1):
            for j in range(len(s), length - 1, -1):
                if not counters[j] ^ counters[j - length]:
                    return length
        return 0
