from collections import defaultdict


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        subCt = defaultdict(int)
        currS = defaultdict(int)
        mx = 0
        l = 0
        r = 0
        while l < len(s) - minSize:
            length = r - l + 1
            if length > minSize:
                currS[s[l]] -= 1
                if currS[s[l]] <= 0:
                    del currS[s[l]]
                l += 1
            c = r == len(s) - 1 and l < len(s) - minSize
            if c:
                print('eer')
                currS[s[l]] -= 1
                if currS[s[l]] <= 0:
                    del currS[s[l]]
                l += 1
            currC = s[r]
            currS[currC] += 1
            condition = r - l + 1 >= minSize and len(list(currS.keys())) <= maxLetters
            if condition:
                sub = s[l:r + 1]
                print(sub)
                subCt[sub] += 1
                if subCt[sub] > mx:
                    mx = subCt[sub]
            if r < len(s) - 1:
                r += 1
        return mx
