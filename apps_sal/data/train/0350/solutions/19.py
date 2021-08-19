class Accumulator:

    def __init__(self):
        self.KeyToCount = {}
        self.q = deque()

    def append(self, value):
        self.q.append(value)
        self.KeyToCount[value] = self.KeyToCount.get(value, 0) + 1

    def popleft(self):
        v = self.q.popleft()
        if self.KeyToCount[v] == 1:
            del self.KeyToCount[v]
        else:
            self.KeyToCount[v] -= 1

    def distinctCount(self):
        return len(self.KeyToCount)


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        nextHiIdx = 0
        nextLoIdx = 0
        loAcc = Accumulator()
        hiAcc = Accumulator()
        lo = [None] * n
        hi = [None] * n
        for i in range(n):
            if i >= 1:
                hiAcc.popleft()
                loAcc.popleft()
            while nextLoIdx < n and loAcc.distinctCount() < K:
                loAcc.append(A[nextLoIdx])
                nextLoIdx += 1
            while nextHiIdx < n and hiAcc.distinctCount() <= K:
                hiAcc.append(A[nextHiIdx])
                nextHiIdx += 1
            if loAcc.distinctCount() == K:
                lo[i] = nextLoIdx - 1
            if hiAcc.distinctCount() == K + 1:
                hi[i] = nextHiIdx - 1
            elif hiAcc.distinctCount() == K and nextHiIdx == n:
                hi[i] = nextHiIdx
        return sum((hi[i] - lo[i] for i in range(n) if hi[i] != None))
