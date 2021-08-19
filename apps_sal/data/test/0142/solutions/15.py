import sys

n, L = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    c[i] = min(c[i], 2 * c[i - 1])
for i in range(n - 2, -1, -1):
    c[i] = min(c[i], c[i + 1])
#print (c)


res = L // 2 ** (n - 1) * c[n - 1]
L %= 2 ** (n - 1)
tres = 0
for sh in range(n):
    if (L & (2 ** sh)) != 0:
        tres += c[sh]
    else:
        tres = min(tres, c[sh])

res += tres
print(res)
