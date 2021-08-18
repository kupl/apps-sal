import itertools


class union_find:
    def __init__(self, n):
        self.par = [-1] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if x > y:
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return-self.par[self.find(x)]


mod = 998244353


def main():
    n, k = map(int, input().split())
    factorial = [1]
    for i in range(1, n + 1):
        factorial.append(factorial[i - 1] * i % mod)
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    gyou = union_find(n)
    for x, y in itertools.combinations(range(n), 2):
        flag = True
        for i in range(n):
            if a[x][i] + a[y][i] > k:
                flag = False
                break
        if flag:
            gyou.unite(x, y)
    retu = union_find(n)

    for x, y in itertools.combinations(range(n), 2):
        flag = True
        for i in range(n):
            if a[i][x] + a[i][y] > k:
                flag = False
                break
        if flag:
            retu.unite(x, y)
    ans = 1
    for i in range(len(retu.par)):
        if retu.par[i] < 0:
            ans *= factorial[-retu.par[i]]
        ans %= mod
    for i in range(len(gyou.par)):
        if gyou.par[i] < 0:
            ans *= factorial[-gyou.par[i]]
        ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
