(n, m) = map(int, input().split())
amatr = [[0] * n for i in range(n)]
alist = [[] for i in range(n)]
for i in range(m):
    (a, b) = map(int, input().split())
    amatr[a - 1][b - 1] = 1
    amatr[b - 1][a - 1] = 1
    alist[a - 1].append(b - 1)
    alist[b - 1].append(a - 1)
known = [len(alist[i]) for i in range(n)]
ans = 10 ** 10
for first in range(n):
    for second in alist[first]:
        if amatr[first][second] == 1:
            for third in alist[second]:
                if amatr[third][second] == 1:
                    if amatr[first][third] == 1:
                        ans = min(ans, known[first] + known[second] + known[third] - 6)
            amatr[first][second] = 0
            amatr[second][first] = 0
print(ans if ans < 10 ** 10 else -1)
