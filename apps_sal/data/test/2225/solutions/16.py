import sys


class SegmTree():
    def __init__(self, size):
        N = 1
        while N < size:
            N <<= 1
        self.N = N
        self.tree = [0] * (2 * N)

    def modify(self, i, value):
        i += self.N
        self.tree[i] = value
        toXOR = False
        while i > 1:
            if toXOR:
                self.tree[i >> 1] = self.tree[i] ^ self.tree[i ^ 1]
            else:
                self.tree[i >> 1] = self.tree[i] | self.tree[i ^ 1]
            toXOR = not toXOR
            i >>= 1


reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
st = SegmTree(1 << n)
for i, value in enumerate(a):
    st.modify(i, value)
for _ in range(m):
    p, b = list(map(int, input().split()))
    st.modify(p - 1, b)
    print(st.tree[1])
