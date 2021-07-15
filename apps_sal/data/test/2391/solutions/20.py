class KMP:
    def __init__(self, P):
        self.P = P
        self.N = len(P)
        self.T = [0] * (self.N + 1)
        self._compile()

    def _compile(self):
        j = 0
        self.T[0] = -1
        for i in range(1, self.N):
            self.T[i] = j
            j += 1 if self.P[i] == self.P[j] else -j
        self.T[self.N] = j

    def search(self, S):
        NS = len(S)
        i = m = 0
        A = []
        while m + i < NS:
            if self.P[i] == S[m + i]:
                i += 1
                if i != self.N:
                    continue
                A.append(m)
            m += i - self.T[i]
            i = max(0, self.T[i])
        return A

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [A[i]^A[(i+1)%N] for i in range(N)]
D = [B[i]^B[(i+1)%N] for i in range(N)]
C = C + C[:-1]
K = KMP(D).search(C)
for k in K:
    print(k, A[k]^B[0])
