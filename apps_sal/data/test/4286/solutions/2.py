def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [tuple(map(int, input().split())) for i in range(m)]

    rt = a.index(min(a))
    e = [(a[i] + a[rt], rt, i) for i in range(n) if i != rt] + [(w, u - 1, v - 1) for u, v, w in b]
    e.sort()

    p = [i for i in range(n)]
    r = [0] * n

    def find(x):
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]

    def check_n_unite(x, y):
        x, y = find(x), find(y)
        if x == y:
            return 0
        if r[x] < r[y]:
            x, y = y, x
        p[y] = x
        if r[x] == r[y]:
            r[x] += 1
        return 1

    ans = 0
    for w, u, v in e:
        if check_n_unite(u, v):
            ans += w
    print(ans)


main()
