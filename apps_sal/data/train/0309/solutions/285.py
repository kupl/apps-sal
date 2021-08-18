class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)

        m = {}
        for i in range(1, n):
            e = m.pop(A[i], {})
            for step, length in e.items():
                e1 = m.setdefault(A[i] + step, {})
                e1[step] = max(e1.get(step, 0), length + 1)
            for j in range(i):
                step = A[i] - A[j]
                e1 = m.setdefault(A[i] + step, {})
                e1[step] = max(e1.get(step, 0), 2)

        return max(max(e.values()) for e in m.values())
