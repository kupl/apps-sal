n, m = input().split(' ')
n = int(n)
m = int(m)
L = []
for i in range(1, 2 * n + 1):
    L.append(2 * n + i)
    L.append(i)

for i in range(4 * n):
    if L[i] <= m:
        print(L[i], end=' ')
