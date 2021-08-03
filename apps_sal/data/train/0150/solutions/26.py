class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        l = [0] * len(A)
        r = [0] * len(A)

        for i in range(len(l)):
            l[i] = max(A[i], l[i - 1])
        r[-1] = A[-1]
        for i in range(len(r) - 2, -1, -1):
            r[i] = min(A[i], r[i + 1])

        print(l)
        print(r)
        for i in range(len(l)):
            if l[i] <= r[i + 1]:
                return i + 1
        return len(l)
