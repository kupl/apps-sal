class Solution:
    def isvalid(self, D):
        if len(D) == 1:
            a = min(D)
            if a == 1 or D[a] == 1:
                return True
            return False
        a, b = min(D), max(D)
        if a == D[a] == 1:
            return True
        return True if (D[b] == 1 and (a + 1) == b) else False

    def maxEqualFreq(self, A):
        best = 0
        B = Counter()
        C = Counter()
        for i, x in enumerate(A):
            old = B[x]
            if old:
                if C[old] == 1:
                    C.pop(old)
                else:
                    C[old] -= 1
            B[x] += 1
            C[B[x]] += 1
            if len(C) <= 2 and self.isvalid(C):
                best = i + 1
        return best
