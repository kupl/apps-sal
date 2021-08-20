(n, k) = list(map(int, input().split(' ')))
b = []
r = []
c = []
for i in range(n):
    b.append(input())
for i in range(n):
    for j in range(k):
        if b[i][j] == 'B':
            r.append(i)
            c.append(j)
if len(c) == 0:
    print(1)
else:
    maxr = max(r) - min(r)
    maxc = max(c) - min(c)
    size = max(maxc, maxr) + 1
    if size > n or size > k:
        print(-1)
    else:
        print(size ** 2 - len(c))
