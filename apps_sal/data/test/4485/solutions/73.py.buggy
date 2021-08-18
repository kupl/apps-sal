n, m = map(int, input().split())
d = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if a == 1 or b == 1 or a == n or b == n:
        d[a - 1].append(b)
        d[b - 1].append(a)
for i in d[n - 1]:
    if 1 in d[i - 1]:
        print('POSSIBLE')
        return
print('IMPOSSIBLE')
