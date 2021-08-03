class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        N = len(s)
        d1 = {}
        maxval = 0
        for i in range(N - minSize + 1):
            d = {}
            for j in range(i, i + minSize):
                if(s[j] not in d):
                    d[s[j]] = 1
                else:
                    d[s[j]] += 1
            if(len(d) <= maxLetters):
                if(s[i:i + minSize] not in d1):
                    d1[s[i:i + minSize]] = 1
                else:
                    d1[s[i:i + minSize]] += 1
                maxval = max(maxval, d1[s[i:i + minSize]])
            else:
                continue
            for j in range(i + minSize, min(i + maxSize, N)):
                if(s[j] not in d):
                    d[s[j]] = 1
                else:
                    d[s[j]] += 1
                if(len(d) <= maxLetters):
                    if(s[i:j + 1] not in list(d1.keys())):
                        d1[s[i:j + 1]] = 1
                    else:

                        d1[s[i:j + 1]] += 1
                    maxval = max(maxval, d1[s[i:j + 1]])
                else:
                    break
        return maxval
