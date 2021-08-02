n = int(input())
g = [0 for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1] += 1
    g[b - 1] += 1
q = 0
k = 0
kind = 0
m = 0
for i in range(n):
    if g[i] == 1:
        m += 1
    if g[i] > 2:
        if g[i] > k:
            kind = i
            k = g[i]
        q += 1
if q > 1:
    print('No')
else:
    print('Yes')
    if k > 2:
        print(m)
        for i in range(n):
            if g[i] == 1:
                print(kind + 1, i + 1)
    else:
        print(1)
        for i in range(n):
            if g[i] == 1:
                print(i + 1, end=' ')
