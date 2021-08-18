class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        p = [None] * len(A)
        q = [None] * len(A)

        for i, v in enumerate(A):
            if i == 0:
                p[0] = v
            else:
                p[i] = max(p[i - 1], v)

        for i, v in enumerate(reversed(A)):
            if i == 0:
                q[len(A) - 1] = v
            else:
                q[len(A) - 1 - i] = min(q[len(A) - i], v)

        for i in range(len(A) - 1):
            if p[i] <= q[i + 1]:
                return i + 1

        return len(A)
