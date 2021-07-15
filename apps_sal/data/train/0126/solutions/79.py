class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # brute force this damn thing
        
        # 1. all substrings
        # if it works with greater than minSize, then must work with exactly minSize
        freq = defaultdict(int)
        best = 0
        for i in range(len(s)-minSize+1):
            ss = s[i:i+minSize]
            # print('substring', ss)
            if len(set(ss)) <= maxLetters:
                freq[ss] += 1
                best = max(best, freq[ss])

        # print(freq)
        return best
