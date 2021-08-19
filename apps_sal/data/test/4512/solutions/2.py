from string import ascii_lowercase as lows
import sys
input = sys.stdin.readline
N = 1 << 17


class bit:

    def __init__(self):
        self.l = [0] * (1 + N)

    def set(self, i):
        self.add(i, 1)

    def unset(self, i):
        self.add(i, -1)

    def add(self, i, val):
        while i <= N:
            self.l[i] += val
            i += i & -i

    def get(self, i):
        r = 0
        while i > 0:
            r += self.l[i]
            i -= i & -i
        return r

    def range(self, l, r):
        return self.get(r) - self.get(l - 1)


bits = {c: bit() for c in lows}
s = [c for c in input().strip()]
for (i, c) in enumerate(s):
    bits[c].set(i + 1)
q = int(input().strip())
for _ in range(q):
    ins = input().split()
    if ins[0] == '1':
        pos = int(ins[1])
        bits[s[pos - 1]].unset(pos)
        bits[ins[2]].set(pos)
        s[pos - 1] = ins[2]
    else:
        (l, r) = list(map(int, ins[1:]))
        sm = 0
        for b in list(bits.values()):
            if b.range(l, r) > 0:
                sm += 1
        print(sm)
