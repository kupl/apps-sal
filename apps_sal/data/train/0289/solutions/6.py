class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        def getMax(p, N):
            _max = 0
            for i in range(len(p) - N):
                _max = max(p[i + N] - p[i], _max)
            return _max

        pre = [0] * (len(A) + 1)
        for i in range(0, len(A)):
            pre[i + 1] = pre[i] + A[i]
        _max = 0
        for i in range(len(A) - max(L, M)):
            _max = max(getMax(pre[:i + L + 1], L) + getMax(pre[i + L:], M), _max)
        for i in range(len(A) - max(L, M)):
            _max = max(getMax(pre[:i + M + 1], M) + getMax(pre[i + M:], L), _max)
        return _max
