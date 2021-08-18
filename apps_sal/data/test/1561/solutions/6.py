
n, m, k = list(map(int, input().split()))
d = [input() for _ in range(n)]

res = 0
for i in range(n):
    cs = 0
    for j in range(m):
        if d[i][j] == '.':
            cs += 1
        else:
            res += max(cs - k + 1, 0)
            cs = 0

    res += max(cs - k + 1, 0)

for j in range(m):
    cs = 0
    for i in range(n):
        if d[i][j] == '.':
            cs += 1
        else:
            res += max(cs - k + 1, 0)
            cs = 0
    res += max(cs - k + 1, 0)

if k == 1:
    print(res // 2)
else:
    print(res)
