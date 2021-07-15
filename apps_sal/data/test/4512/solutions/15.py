import sys

input = sys.stdin.readline

class SegmentTree:
    a = ord('a')

    def __init__(self):
        data = [1 << ord(c) - self.a for c in input()[:-1]]

        self.n = 1 << len(bin(len(data) - 1)) - 2
        self.data = [0] * self.n + data + [0] * (self.n - len(data))

        for k in range(self.n - 1, 0, -1):
            self.data[k] = self.data[2 * k + 1] | self.data[2 * k]

    def update(self, k, c):
        k += self.n
        self.data[k] = 1 << ord(c) - self.a

        while k > 1:
            k >>= 1
            self.data[k] = self.data[2 * k + 1] | self.data[2 * k]

    def query(self, l, r):
        l += self.n
        r += self.n
        s = self.data[r] | self.data[l]

        while l < r - 1:
            if r & 1: s |= self.data[r - 1]
            if not l & 1: s |= self.data[l + 1]
            l >>= 1
            r >>= 1
        return s

tree = SegmentTree()

for i in range(int(input())):
    q = input()[:-1].split()
    if q[0] == "1":
        tree.update(int(q[1]) - 1, q[2])
    else:
        s = tree.query(int(q[1]) - 1, int(q[2]) - 1)
        print(bin(s)[2:].count("1"))
