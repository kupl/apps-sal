
from sortedcontainers import SortedSet


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        def getNextLargerIdx(x):
            i = sortedSet.bisect_left(x)
            if i == len(sortedSet):
                return -1
            return indices[sortedSet[i]]

        def getNextSmallerIdx(x):
            i = sortedSet.bisect_right(x)
            if i == 0:
                return -1
            return indices[sortedSet[i - 1]]

        n = len(A)

        if n == 0:
            return 0

        sortedSet = SortedSet([A[n - 1]])
        indices = {A[n - 1]: n - 1}

        dp_odd, dp_even = [False for _ in range(n)], [False for _ in range(n)]
        dp_odd[n - 1] = dp_even[n - 1] = True

        for i in range(n - 2, -1, -1):
            j = getNextLargerIdx(A[i])
            dp_odd[i] = (j != -1 and dp_even[j])

            j = getNextSmallerIdx(A[i])
            dp_even[i] = (j != -1 and dp_odd[j])

            sortedSet.add(A[i])
            indices[A[i]] = i

        return dp_odd.count(True)
