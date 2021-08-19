class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:

        rangesCovered = {}
        # key = spot, value = range as tuple

        for i, ran in enumerate(ranges):
            if (ran == 0):
                continue
            rangesCovered[i] = (max(0, i - ranges[i]), min(n, i + ranges[i]))

        # print(rangesCovered)
        dp = [n + 2] * (n + 1)
        dp[0] = 0
        # dp[i] = min number of taps to water all [0, i]

        for curRange in list(rangesCovered.values()):
            # print(curRange)
            startInd = curRange[0]
            endInd = curRange[1]
            for i in range(startInd + 1, endInd + 1):
                dp[i] = min(dp[i], dp[startInd] + 1)
            # print(dp)

        if (dp[n] == (n + 2)):
            return -1
        else:
            return dp[n]
#         taps = []
#         for i in range(n + 1):
#             isCovered[i] = False
#             taps.append(i)


#         curMins = float(\"inf\")
#         def recur(tapsRem, curCount):
#             # print(curCount, tapsRem)
#             # print(isCovered)
#             nonlocal curMins
#             if (all(isCovered.values())):

#                 curMins = min(curMins, curCount)
#                 return
#             else:
#                 if (curCount > curMins):
#                     return

#                 for i, val in enumerate(tapsRem):
#                     newRem = tapsRem[:i] + tapsRem[i + 1:]
#                     wasFalses = []
#                     for j in range(rangesCovered[i][0], rangesCovered[i][1] + 1):
#                         if isCovered[j] == False:
#                             wasFalses.append(j)
#                         isCovered[j] = True

#                     recur(newRem, curCount + 1)
#                     for ind in wasFalses:
#                         isCovered[ind] = False

#         # print(taps)
#         recur(taps, 0)
#         if (curMins ==  float(\"inf\")):
#             return -1
#         return curMins
