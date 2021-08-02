import sys
input = sys.stdin.readline


class BIT:
    def __init__(self, size):
        self.bit = [0] * (size + 1)
        self.size = size

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.bit[i] += x
            i += i & -i


n, m = list(map(int, input().split()))
a = list([int(x) - 1 for x in input().split()])

bit0 = BIT(m)
bit1 = BIT(m)
for i in range(n - 1):
    x, y = a[i], a[i + 1]
    bit1.add(0, (y - x) % m)
    if (y - x) % m < 2:
        continue
    x = (x + 2) % m
    if x <= y:
        bit0.add(x, -1)
        bit1.add(x, x - 1)
        bit0.add(y + 1, 1)
        bit1.add(y + 1, -(x - 1))
    else:
        bit0.add(x, -1)
        bit1.add(x, x - 1)

        b = (0 - (x - 1)) % m
        bit0.add(0, -1)
        bit1.add(0, -b)
        bit0.add(y + 1, 1)
        bit1.add(y + 1, b)

ans = min(bit0.sum(i) * i + bit1.sum(i) for i in range(m))
print(ans)
