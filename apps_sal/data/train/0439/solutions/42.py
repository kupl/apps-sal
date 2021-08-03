class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:

        maxN = 1
        leftPos = 0
        lastC = 0
        curC = 0
        if len(A) == 1:
            return 1
        if len(A) == 2:
            if A[0] == A[1]:
                return 1

        for i in range(len(A) - 1):
            if A[i + 1] > A[i]:
                curC = 1
            elif A[i + 1] == A[i]:
                maxN = max(maxN, i - leftPos + 1)
                if (len(A) - i - 1) < maxN:
                    return maxN
                curC = 0
                leftPos = i + 1
                continue
            else:
                curC = -1
            if curC == lastC:
                maxN = max(maxN, i + 1 - leftPos)
                leftPos = i
                if (len(A) - i - 1) < maxN:
                    return maxN
            lastC = curC
        return max(maxN, len(A) - leftPos)
