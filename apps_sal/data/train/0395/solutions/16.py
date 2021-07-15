from sortedcontainers import SortedDict

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        sd = SortedDict()
        sd[A[-1]] = len(A) - 1
        goodOddIndices = [False] * len(A)
        goodEvenIndices = [False] * len(A)
        goodOddIndices[-1] = True
        goodEvenIndices[-1] = True
        
        i = len(A) - 2
        while i >= 0:
            if A[i] in sd:
                goodEvenIndices[i] = goodOddIndices[sd[A[i]]]
                goodOddIndices[i] = goodEvenIndices[sd[A[i]]]
                sd[A[i]] = i
            else:
                sd[A[i]] = i
                idx = sd.index(A[i])
                if idx > 0:
                    _, lowerIdx = sd.peekitem(idx-1)
                    goodEvenIndices[i] = goodOddIndices[lowerIdx]
                    # goodOddIndices[i] = goodEvenIndices[lowerIdx]
                if idx < len(sd) - 1:
                    _, higherIdx = sd.peekitem(idx+1)
                    # goodEvenIndices[i] = goodOddIndices[higherIdx]
                    goodOddIndices[i] = goodEvenIndices[higherIdx]
            i -= 1
        totalGoodIndices = 0
        for b in goodOddIndices:
            if b:
                totalGoodIndices += 1
        return totalGoodIndices
