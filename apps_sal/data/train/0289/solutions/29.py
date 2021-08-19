class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        LList, MList = [], []
        thisSum = sum(A[:L])
        LList.append((thisSum, 0))
        for idx in range(L, len(A)):
            thisSum += A[idx] - A[idx - L]
            LList.append((thisSum, idx - L + 1))
        thisSum = sum(A[:M])
        MList.append((thisSum, 0))
        for idx in range(M, len(A)):
            thisSum += A[idx] - A[idx - M]
            MList.append((thisSum, idx - M + 1))
        # LList.sort(reverse=True)
        # MList.sort(reverse=True)
        allHeap = []
        for LEle in LList:
            for MEle in MList:
                heapq.heappush(allHeap, (- LEle[0] - MEle[0], LEle[1], MEle[1]))
        while allHeap:
            twoSum, lidx, midx = heapq.heappop(allHeap)
            if lidx + L - 1 < midx or midx + M - 1 < lidx:
                return -twoSum
