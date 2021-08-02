n, m = (int(token) for token in input().split())

res = []
for i in range(1, 2 * n + 1):
    if 2 * n + i <= m:
        res.append(str(2 * n + i))
    if i <= m:
        res.append(str(i))
print(' '.join(res))
