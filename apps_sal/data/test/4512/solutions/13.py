import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


class SegmentTree():
    def __init__(self, n):
        self.n = 2**(n-1).bit_length()
        self.data = [0 for _ in range(2*self.n)]

    def set(self, k, v):
        v_val = ord(v)-ord('a')
        self.data[k+self.n-1] = 1 << v_val

    def build(self):
        for k in reversed(list(range(self.n-1))):
            self.data[k] = self.data[k*2+1] | self.data[k*2+2]

    def update(self, k, a):
        k += self.n-1
        v_val = ord(a)-ord("a")
        self.data[k] = 1 << v_val

        while k > 0:
            k = (k-1)//2
            self.data[k] = self.data[k*2+1] | self.data[k*2+2]

    def query(self, l, r):
        L = l+self.n
        R = r+self.n
        ret = 0
        while L < R:
            if R & 1:
                R -= 1
                ret |= self.data[R-1]
            if L & 1:
                ret |= self.data[L-1]
                L += 1
            L >>= 1
            R >>= 1
        return ret


S = [v for v in input()[:-1]]
N = len(S)
Q = int(input())
query = [[v for v in input()[:-1].split()] for _ in range(Q)]

Seg = SegmentTree(N)
for i, s in enumerate(S):
    Seg.set(i, s)

Seg.build()

for q, v1, v2 in query:
    if q == "1":
        Seg.update(int(v1)-1, v2)
    else:
        val = Seg.query(int(v1)-1, int(v2))
        print(bin(val)[2:].count("1"))

