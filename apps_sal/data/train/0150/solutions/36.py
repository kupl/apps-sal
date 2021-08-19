class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        l = [A[0]]
        r = [A[-1]]
        for (i, v) in enumerate(A):
            if i == 0:
                continue
            l.append(max(l[i - 1], A[i]))
            r.append(min(r[i - 1], A[len(A) - i - 1]))
        r.reverse()
        for i in range(1, len(l)):
            if l[i - 1] <= r[i]:
                return i
