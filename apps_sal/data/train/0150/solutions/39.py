class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        ma = [0] * n
        mi = [0] * n

        mi[-1] = A[-1]
        for i in range(n - 2, -1, -1):
            mi[i] = min(A[i + 1], mi[i + 1])

        ma[0] = A[0]
        for i in range(1, n):
            ma[i] = max(A[i], ma[i - 1])

        # print(mi)
        # print(ma)

        for i in range(n - 1):
            if mi[i] >= ma[i]:
                return i + 1
        return n
