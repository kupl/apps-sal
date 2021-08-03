class Solution:
    def maxFreq(self, s: str, mxl: int, mns: int, mxs: int) -> int:
        freq = collections.Counter()
        for i in range(mns, len(s) + 1):
            for j in range(mxs - mns + 1):
                if i + j > len(s):
                    break
                curr = s[i - mns:i + j]
                if len(set(curr)) > mxl:
                    break
                freq[curr] += 1
        return max(freq.values() or [0])
