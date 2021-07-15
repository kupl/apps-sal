n,m = map(int, input().split())
H = list(map(int, input().split()))
g = [1]*n

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if H[a]<H[b]:
        g[a] = 0
    elif H[a]>H[b]:
        g[b] = 0
    else:
        g[a] = g[b] = 0
print(sum(g))
