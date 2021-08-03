from collections import defaultdict


def getdiff(l):
    diff = []
    for i in range(m):
        if l[i] != i + 1:
            diff.append(l[i])
    return diff


n, m = list(map(int, input().split()))
t = [list(map(int, input().split())) for i in range(n)]

diffs = [defaultdict(bool) for i in range(n)]
for j in range(m):
    for j2 in range(j, m):
        for i in range(n):
            t[i][j], t[i][j2] = t[i][j2], t[i][j]
            df = getdiff(t[i])
            t[i][j], t[i][j2] = t[i][j2], t[i][j]
            if len(df) == 2:
                diffs[i][tuple(sorted(df))] = True

for j in range(m):
    for j2 in range(j, m):
        for i in range(n):
            if j != j2 and not diffs[i][(j + 1, j2 + 1)]:
                break
            t[i][j], t[i][j2] = t[i][j2], t[i][j]
            df = getdiff(t[i])
            t[i][j], t[i][j2] = t[i][j2], t[i][j]
            if len(df) > 2:
                break
        else:
            print('YES')
            return
print('NO')
