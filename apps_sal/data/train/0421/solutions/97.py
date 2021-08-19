class Solution:

    def lastSubstring(self, s: str) -> str:
        maxIndex = []
        maxS = ''
        for i in range(len(s)):
            if maxS < s[i]:
                maxS = s[i]
                maxIndex = []
                maxIndex.append(i)
            elif maxS == s[i]:
                maxIndex.append(i)
        soln = s[maxIndex[0]:]
        for index in maxIndex:
            if soln <= s[index:]:
                soln = s[index:]
        return soln
