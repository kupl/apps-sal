import itertools
(n, m) = map(int, input().split())
tbl = [[0] * n for _ in range(n)]
for _ in range(m):
    (a, b) = map(int, input().split())
    tbl[a - 1][b - 1] = 1
    tbl[b - 1][a - 1] = 1
ans = 0
l = [i + 1 for i in range(n - 1)]
for p in itertools.permutations(l, n - 1):
    flag = True
    p = [0] + list(p)
    for i in range(n - 1):
        if tbl[p[i]][p[i + 1]] == 0:
            flag = False
            break
    if flag:
        ans += 1
print(ans)
