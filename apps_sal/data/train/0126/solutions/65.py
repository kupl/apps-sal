class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # brute force this damn thing

        # 1. all substrings
        freq = defaultdict(int)
        best = 0
        for l in range(minSize, maxSize + 1):
            for i in range(len(s) - l + 1):
                ss = s[i:i + l]
                # print('substring', ss)
                if len(set(ss)) <= maxLetters:
                    freq[ss] += 1
                    best = max(best, freq[ss])

        # print(freq)
        return best
