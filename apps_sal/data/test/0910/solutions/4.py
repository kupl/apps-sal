[n, a, b] = list(map(int, input().split(' ')))
r = [(b + 1) * [0] for _ in range(a + 1)]
t = list(range(1, n + 1))
for i in range(1, a + 1):
    for j in range(1, b + 1):
        for it in t:
            if (r[i - 1][j] == 0 or r[i - 1][j] % 2 != it % 2) and (r[i][j - 1] == 0 or r[i][j - 1] % 2 != it % 2):
                r[i][j] = it
                break
        if r[i][j] != 0:
            t.remove(r[i][j])
if len(t) == 0:
    for i in r[1:]:
        print(*i[1:])
else:
    print(-1)
