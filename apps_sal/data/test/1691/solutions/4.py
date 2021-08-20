class Fen:

    def __init__(self, n):
        self.value = [0] * n

    def get(self, fro, to):
        return self.get1(to) - self.get1(fro - 1)

    def get1(self, to):
        to = min(to, len(self.value))
        result = 0
        while to >= 0:
            result += self.value[to]
            to = (to & to + 1) - 1
        return result

    def add(self, at, value):
        while at < len(self.value):
            self.value[at] += value
            at = at | at + 1


def solve():
    (n, k) = map(int, input().split())
    k = min(k, n - k)
    count = [0] * n
    res = [None] * n
    ans = 1
    cur = 0
    fen = Fen(n)
    for iteration in range(n):
        nxt = (cur + k) % n
        here = 0
        if cur < nxt:
            here = fen.get(cur + 1, nxt - 1)
        else:
            here = fen.get(0, nxt - 1) + fen.get(cur + 1, n - 1)
        fen.add(cur, 1)
        fen.add(nxt, 1)
        cur = nxt
        ans += here + 1
        res[iteration] = ans
    print(' '.join(map(str, res)))


solve()
