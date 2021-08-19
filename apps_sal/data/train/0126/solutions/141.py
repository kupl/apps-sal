class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        lenS = len(s)

        # for counting uniq chars :
        uniqSubStrDict = {}

        # for i,char in enumerate(s):
        #    uniqDict[char] = i
        count = 0
        # edge casses:

        # main alg.
        Max = 0
        for i in range(minSize, maxSize + 1):
            for j in range(lenS - i + 1):  # maxSize):

                tstSubStr = s[j: j + i]
                uniqChars = {}
                for k in tstSubStr:
                    uniqChars[k] = 1  # uniqChars.get(k,0) + 1

                if len(uniqChars) > maxLetters:
                    #print(' in over maxLetters loop -- tstSubStr = {} '.format(tstSubStr))
                    continue

                #print(' tstSubStr = {} '.format(tstSubStr))
                uniqSubStrDict[tstSubStr] = uniqSubStrDict.get(tstSubStr, 0) + 1
                #print(' dict count = {} '.format(uniqSubStrDict[tstSubStr]))

                if uniqSubStrDict[tstSubStr] > Max:
                    Max = uniqSubStrDict[tstSubStr]

        count = Max
        #count = uniqSubStrDict[tstSubStr]

        return count
