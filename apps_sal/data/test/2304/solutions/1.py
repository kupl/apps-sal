import sys
sys.setrecursionlimit(10 ** 9)
read = sys.stdin.read


class Unionfind:

    def __init__(self, n):
        self.parents = [-1] * n
        self.ranks = [0] * n
        self.dist = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return (self.dist[x], x)
        else:
            tmp = self.find(self.parents[x])
            self.dist[x] += tmp[0]
            self.parents[x] = tmp[1]
            return (self.dist[x], self.parents[x])

    def union(self, x, y, d):
        rx = self.find(x)[-1]
        ry = self.find(y)[-1]
        diff = d + self.dist[x] - self.dist[y]
        if rx == ry:
            if diff != 0:
                return True
            return False
        if self.ranks[ry] > self.ranks[rx]:
            (rx, ry) = (ry, rx)
            diff = -diff
        self.parents[ry] = rx
        self.dist[ry] = diff
        if self.ranks[ry] == self.ranks[rx]:
            self.ranks[rx] += 1
        return False


def main():
    (n, m, *lrd) = list(map(int, read().split()))
    v = Unionfind(n)
    for (l, r, d) in zip(*[iter(lrd)] * 3):
        if v.union(l - 1, r - 1, d):
            print('No')
            break
    else:
        print('Yes')


def __starting_point():
    main()


__starting_point()
