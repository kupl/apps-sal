class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        d = defaultdict(int)
        for i in range(len(s) - minSize + 1):
            letters = set(s[i:i + minSize - 1])
            for j in range(minSize, min(maxSize, len(s) - i) + 1):
                letters.add(s[i + j - 1])
                if len(letters) > maxLetters:
                    break
                d[s[i:i + j]] += 1
        return max(d.values()) if d else 0
