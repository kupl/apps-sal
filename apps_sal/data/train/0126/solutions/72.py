class Solution:

    def maxFreq(self, s: str, m: int, n: int, ss: int) -> int:

        def getSubStrings(maxLetters: int, minSize: int, maxSize: int):
            for i in range(len(s)):
                for j in range(i + minSize, len(s) + 1):
                    if j - i > maxSize:
                        break
                    sub = s[i:j]
                    if len(set(sub)) <= maxLetters:
                        yield sub
        counter = collections.defaultdict(int)
        ret = 0
        for substring in getSubStrings(m, n, ss):
            counter[substring] += 1
            ret = max(ret, counter[substring])
        return ret
