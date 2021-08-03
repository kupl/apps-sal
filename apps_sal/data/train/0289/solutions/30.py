class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        def slidingWindow(windowLength):
            windowMap = {}
            currSum = sum(A[:windowLength])
            windowMap[(0, windowLength - 1)] = currSum

            for i in range(windowLength, len(A)):
                currSum -= A[i - windowLength]
                currSum += A[i]
                windowMap[(i - windowLength + 1, i)] = currSum

            return windowMap

        firstWindowMap = slidingWindow(L)
        secondWindowMap = slidingWindow(M)

        first = []
        second = []

        for x in firstWindowMap:
            first.append([firstWindowMap[x], x])

        for x in secondWindowMap:
            second.append([secondWindowMap[x], x])

        most = 0

        for i in range(len(first)):
            for j in range(len(second)):
                val1 = first[i][0]
                val2 = second[j][0]
                range1 = first[i][1]
                range2 = second[j][1]
                r1x = range1[0]
                r1y = range1[1]
                r2x = range2[0]
                r2y = range2[1]
                if not ((r2x <= r1x <= r2y) or (r1x <= r2x <= r1y)):
                    most = max(most, val1 + val2)

        return most
