class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = defaultdict(int)
        best = 0
        for i in range(len(s) - minSize + 1):
            ss = s[i:i + minSize]
            if len(set(ss)) <= maxLetters:
                freq[ss] += 1
                best = max(best, freq[ss])
        return best
