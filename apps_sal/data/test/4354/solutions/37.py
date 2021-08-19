(n, m) = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
c = [list(map(int, input().split())) for _ in range(m)]
ans = []
INF = 10 ** 9 + 7
for x in s:
    d = INF
    ind = INF
    for (i, y) in enumerate(c):
        exd = d
        d = min(d, abs(x[0] - y[0]) + abs(x[1] - y[1]))
        if d != exd:
            ind = i
    ans.append(ind + 1)
for x in ans:
    print(x)
