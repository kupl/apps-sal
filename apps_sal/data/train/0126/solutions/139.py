import collections


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        # for each substring of length, find unique chars
        maxC = Counter()
        ans = 0
        for sz in range(minSize, maxSize + 1):
            unq = Counter()
            for i in range(sz):
                unq[s[i]] += 1

            if (len(unq) <= maxLetters):
                maxC[s[0:sz]] += 1
                if(maxC[s[0:sz]] > ans):
                    ans = maxC[s[0:sz]]

            i, j = 0, sz - 1
            while (j < len(s) - 1):
                unq[s[i]] -= 1
                if (unq[s[i]] == 0):
                    del unq[s[i]]

                i += 1
                j += 1

                unq[s[j]] += 1

                if (len(unq) <= maxLetters):
                    maxC[s[i:j + 1]] += 1
                    if(maxC[s[i:j + 1]] > ans):
                        ans = maxC[s[i:j + 1]]

        return ans
