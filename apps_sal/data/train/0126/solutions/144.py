class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = {}
        for i in range(0, len(s) - minSize + 1):
            sub = s[i:i + minSize]
            chars = set()
            for c in sub:
                chars.add(c)
            if len(chars) <= maxLetters:
                if sub not in freq:
                    freq[sub] = 0
                freq[sub] += 1
        best = 0
        for sub in freq:
            if freq[sub] > best:
                best = freq[sub]
        return best
