import sys
readline = sys.stdin.readline


class Segtree:
    def __init__(self, A, intv, initialize=True, segf=max):
        self.N = len(A)
        self.N0 = 2**(self.N - 1).bit_length()
        self.intv = intv
        self.segf = segf
        if initialize:
            self.data = [intv] * self.N0 + A + [intv] * (self.N0 - self.N)
            for i in range(self.N0 - 1, 0, -1):
                self.data[i] = self.segf(self.data[2 * i], self.data[2 * i + 1])
        else:
            self.data = [intv] * (2 * self.N0)

    def update(self, k, x):
        k += self.N0
        self.data[k] = x
        while k > 0:
            k = k >> 1
            self.data[k] = self.segf(self.data[2 * k], self.data[2 * k + 1])

    def query(self, l, r):
        L, R = l + self.N0, r + self.N0
        s = self.intv
        while L < R:
            if R & 1:
                R -= 1
                s = self.segf(s, self.data[R])
            if L & 1:
                s = self.segf(s, self.data[L])
                L += 1
            L >>= 1
            R >>= 1
        return s

    def binsearch(self, l, r, check, reverse=False):
        L, R = l + self.N0, r + self.N0
        SL, SR = [], []
        while L < R:
            if R & 1:
                R -= 1
                SR.append(R)
            if L & 1:
                SL.append(L)
                L += 1
            L >>= 1
            R >>= 1

        if reverse:
            for idx in (SR + SL[::-1]):
                if check(self.data[idx]):
                    break
            else:
                return -1
            while idx < self.N0:
                if check(self.data[2 * idx + 1]):
                    idx = 2 * idx + 1
                else:
                    idx = 2 * idx
            return idx
        else:
            for idx in (SL + SR[::-1]):
                if check(self.data[idx]):
                    break
            else:
                return -1
            while idx < self.N0:
                if check(self.data[2 * idx]):
                    idx = 2 * idx
                else:
                    idx = 2 * idx + 1
            return idx - self.N0


N = int(readline())
A = list(map(int, readline().split()))
B = [2 * a for a in A]
B *= 3
inf = 2 * 10**9
B.append(-2)
T = Segtree(B, inf, True, min)

NN = T.N0

J = [0] * (NN + 1)
J[3 * N] = inf
KK = [None] * (NN + 1)
for i in range(3 * N - 1, -1, -1):
    a = A[i % N]
    k = T.binsearch(i, NN, lambda x: x < a, reverse=False)
    KK[i] = k
    J[i] = min(J[i + 1], k)

Ans = [-1] * N
for i in range(N):
    j = J[i]
    if j == 3 * N:
        continue
    Ans[i] = j - i
print(*Ans)
