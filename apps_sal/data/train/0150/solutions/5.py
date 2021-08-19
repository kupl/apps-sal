class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        large = [0] * n
        small = [0] * n
        (l, s) = (-sys.maxsize, sys.maxsize)
        for i in range(n):
            l = max(l, A[i])
            s = min(s, A[n - 1 - i])
            large[i] = l
            small[n - 1 - i] = s
        for i in range(n):
            if large[i] <= small[i + 1]:
                return i + 1
        return -1
