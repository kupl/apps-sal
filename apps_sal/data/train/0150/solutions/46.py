class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:

        maxlefts = []
        minrights = []

        m = A[0]
        for n in A:
            m = max(m, n)
            maxlefts.append(m)

        m = A[len(A) - 1]
        for n in A[::-1]:
            m = min(m, n)
            minrights.insert(0, m)

        for i in range(1, len(A)):
            if maxlefts[i - 1] <= minrights[i]:
                return i
