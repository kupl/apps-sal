class Solution:
    def isvalid(self, C):
        if len(C) > 2:
            return False
        if len(C) == 1:
            a = min(C)
            if a == 1 or C[a] == 1:
                return True
            return False
        a, b = sorted(C)
        if a == C[a] == 1:
            return True
        return True if (C[b] == 1 and (b - 1) == a) else False

    def remove(self, B, x):
        if B[x] == 1:
            B.pop(x)
        else:
            B[x] -= 1

    def maxEqualFreq(self, A):
        remove = self.remove
        B = Counter(A)
        C = Counter(B.values())
        for i in reversed(range(len(A))):
            if self.isvalid(C):
                return i + 1
            x = A[i]
            remove(C, B[x])
            remove(B, x)
            if B[x]:
                C[B[x]] += 1
        return 0
