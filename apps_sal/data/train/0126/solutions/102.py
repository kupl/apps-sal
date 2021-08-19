class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        max_occ = 0
        D = {}
        for i in range(len(s)):
            for j in range(i + minSize, i + maxSize + 1):
                if j <= len(s):
                    s_s = s[i:j]
                else:
                    continue
                if len(set(s_s)) <= maxLetters:
                    if s_s in D.keys():
                        D[s_s] += 1
                    else:
                        D[s_s] = 1
                    max_occ = max(D[s_s], max_occ)
        return max_occ
