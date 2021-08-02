n, m = list(map(int, input().split()))
a = []
for i in range(n):
    s = input()
    s = s.replace('', ' ')
    s = s[1:-1]
    a += [list(s.split())]
mp = 0
ms = 0
mv = [0] * m
for i in range(m):
    for j in range(n):
        if a[j][i] == '*':
            mv[i] = n - j
            break
for i in range(m - 1):
    mp = max(mp, mv[i + 1] - mv[i])
    ms = max(ms, mv[i] - mv[i + 1])
print(mp, ms)
