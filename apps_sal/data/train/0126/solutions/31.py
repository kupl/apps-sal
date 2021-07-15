class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = Counter()
        for leftInd, char in enumerate(s):
            seen = set([])
            for rightInd in range(leftInd, leftInd + maxSize):
                if rightInd > len(s) - 1:
                    break
                seen.add(s[rightInd])
                if len(seen) > maxLetters:
                    break
                if maxSize >= rightInd - leftInd + 1 >= minSize:
                    freq[s[leftInd:rightInd + 1]] += 1
        ret = 0
        for key, val in freq.items():
            ret = max(ret, val)
        return ret
