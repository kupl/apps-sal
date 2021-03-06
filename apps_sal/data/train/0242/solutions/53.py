class Solution:

    def isvalid(self, D):
        if len(D) > 2:
            return False
        if len(D) == 1:
            a = min(D)
            if a == 1 or D[a] == 1:
                return True
            return False
        (a, b) = (min(D), max(D))
        if a == D[a] == 1:
            return True
        return True if a == b - 1 and D[b] == 1 else False

    def maxEqualFreq(self, A):
        best = 0
        B = Counter()
        C = Counter()
        for (i, x) in enumerate(A):
            if B[x]:
                if C[B[x]] == 1:
                    C.pop(B[x])
                else:
                    C[B[x]] -= 1
            B[x] += 1
            C[B[x]] += 1
            if self.isvalid(C):
                best = i + 1
        return best
