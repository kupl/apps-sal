from collections import defaultdict, Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        def hasUnique(s):
            dic = Counter(s)
            if(len(dic) <= maxLetters):
                return True
            return False

        def checkSubStrings(s):
            dic = defaultdict(int)
            maximum = 0
            for i in range(0, len(s) - minSize + 1):
                end = i + minSize
                strr = s[i:end]
                if(hasUnique(strr)):
                    dic[strr] += 1
                    maximum = max(maximum, dic[strr])

            return maximum

        return(checkSubStrings(s))
