import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
for i in range(n):
    A[i] -= 1


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, l, r):
        s = 0
        while r > 0:
            s += self.tree[r]
            r -= r & -r
        while l > 0:
            s -= self.tree[l]
            l -= l & -l
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sett(self, i, x):
        self.add(i, x - self.sum(i, i + 1))

    def print_bit(self):
        print([self.sum(i, i + 1) for i in range(self.size)])

    def print_sum(self):
        print([self.sum(0, i + 1) for i in range(self.size)])

    def lower_bound_left(self, w):
        n = self.size
        r = 1
        x = 0
        if self.sum(0, n) < w:
            return n
        while r < n:
            r *= 2
        le = r
        while le > 0:
            if (x + le < n and self.tree[x + le] < w):
                w -= self.tree[x + le]
                x += le
            le //= 2
        return x

    def upper_bound_left(self, w):
        n = self.size
        r = 1
        x = 0
        if self.sum(0, n) <= w:
            return n
        while r < n:
            r *= 2
        le = r
        while le > 0:
            if (x + le < n and self.tree[x + le] <= w):
                w -= self.tree[x + le]
                x += le
            le //= 2
        return x

    def lower_bound_right(self, w):
        return self.upper_bound_left(w) - 1

    def upper_bound_right(self, w):
        return self.lower_bound_left(w) - 1


B = Bit(m * 3)

for i in range(n - 1):
    a = A[i]
    b = A[i + 1]
    if a == b:
        continue
    d = (b - a) % m
    ra = d - 1
    l1 = a + 2
    r1 = l1 + ra
    B.add(l1, 1)
    B.add(r1, -1)
    B.add(r1, -ra)
    B.add(r1 + 1, ra)

S = [B.sum(0, i + 1) for i in range(3 * m)]
for i in range(1, 3 * m):
    S[i] += S[i - 1]


ANS = [0] * m
for i in range(3 * m):
    ANS[i % m] += S[i]

now = 0
for i in range(n - 1):
    now += (A[i + 1] - A[i]) % m

print(now - max(ANS))
