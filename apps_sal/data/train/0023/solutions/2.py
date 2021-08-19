import sys


def I():
    return sys.stdin.readline().rstrip()


class Heap:

    def __init__(self):
        self.l = [-1]
        self.n = 0

    def n(self):
        return self.n

    def top(self):
        return self.l[1]

    def ins(self, x):
        self.l.append(x)
        n = len(self.l) - 1
        i = n
        while i > 1:
            j = i // 2
            if self.l[j] > self.l[i]:
                (self.l[j], self.l[i]) = (self.l[i], self.l[j])
                i = j
            else:
                break

    def pop(self):
        r = self.l[1]
        l = self.l.pop()
        n = len(self.l) - 1
        if n:
            self.l[1] = l
            i = 1
            while True:
                j = i * 2
                k = j + 1
                if k < len(self.l) and self.l[i] > max(self.l[j], self.l[k]):
                    if self.l[j] == min(self.l[j], self.l[k]):
                        (self.l[i], self.l[j]) = (self.l[j], self.l[i])
                        i = j
                    else:
                        (self.l[i], self.l[k]) = (self.l[k], self.l[i])
                        i = k
                elif k < len(self.l) and self.l[i] > self.l[k]:
                    (self.l[i], self.l[k]) = (self.l[k], self.l[i])
                    i = k
                elif j < len(self.l) and self.l[i] > self.l[j]:
                    (self.l[i], self.l[j]) = (self.l[j], self.l[i])
                    i = j
                else:
                    break
        return r


t = int(I())
for _ in range(t):
    n = int(I())
    voter = [list(map(int, I().split())) for _ in range(n)]
    h = Heap()
    d = {}
    for (m, p) in voter:
        if m not in d:
            d[m] = []
        d[m].append(p)
    need = {}
    c = 0
    sk = sorted(d.keys())
    for m in sk:
        need[m] = max(0, m - c)
        c += len(d[m])
    c = 0
    ans = 0
    for m in sk[::-1]:
        for p in d[m]:
            h.ins(p)
        while c < need[m]:
            c += 1
            ans += h.pop()
    print(ans)
