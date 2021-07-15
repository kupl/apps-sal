N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


C = [0] * (2 * N - 1)
D = [0] * N
for i in range(2 * N - 1):
    C[i] = A[i % N] ^ A[(i + 1) % N]
    D[i % N] = B[i % N] ^ B[(i + 1) % N]

class KMP:

    def __init__(self, W):
        self.W = W
        self.L = len(W)
        self.T = self._build(W)

    def _build(self, W):
        T = [0] * self.L
        T[0] = -1
        T[1] = 0
        i = 2
        j = 0

        while i < self.L:
            if W[i - 1] == W[j]:
                T[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = T[j]
            else:
                T[i] = 0
                i += 1

        return T

    def search(self, S):
        m = 0
        i = 0
        L = len(S)
        while m + i < L:
            # print(m, i)
            if self.W[i] == S[m + i]:
                i += 1
                if i == self.L:
                    i -= 1
                    ret = m
                    m = m + i - self.T[i]
                    i = self.T[i]
                    yield ret
            else:
                m = m + i - self.T[i]
                if i > 0:
                    i = self.T[i]

# def ok(x, i):
#     for j in range(N):
#         if A[(j + i) % N] ^ B[j] != x:
#             return False
#     return True
#
#
# for i in range(N):
#     x = A[i] ^ B[0]
#     if ok(x, i):
#         print(i, x)

kmp = KMP(D)
for x in kmp.search(C):
    xor = A[x] ^ B[0]
    print(x, xor)
