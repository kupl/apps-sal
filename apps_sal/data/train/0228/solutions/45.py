class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        a = s[:k]
        d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        def checkVowels():
            total = 0
            for key in d:
                total += d[key]
            return total
        for c in s[:k]:
            if c in d:
                d[c] += 1
        total = checkVowels()
        i = 1
        while i <= len(s) - k:
            prev = s[i - 1]
            if prev in d:
                d[prev] -= 1
            nxt = s[i + k - 1]
            if nxt in d:
                d[nxt] += 1
            total = max(total, checkVowels())
            i += 1
        return total
