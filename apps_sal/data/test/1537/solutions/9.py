n, k = map(int, input().split())
a = [input() for _ in range(n)]
m = n - k + 1


def solve(a):
    p = [(r.find('B'), r.rfind('B')) for r in a]
    def get(i, j): return j <= p[i][0] and p[i][1] <= j + k - 1
    res = [[0] * m for _ in range(m)]
    for j in range(m):
        res[0][j] = cnt = sum(x == -1 for x, _ in p) + sum(get(i, j) for i in range(k))
        for i in range(k, n):
            res[i - k + 1][j] = cnt = cnt + get(i, j) - get(i - k, j)
    return res


x = [v for r in solve(a) for v in r]
y = [v for r in list(zip(*solve(list(''.join(y) for y in zip(*a))))) for v in r]
print(max(u + v for u, v in zip(x, y)))
