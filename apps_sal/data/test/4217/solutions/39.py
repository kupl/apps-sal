n, m = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
f = x[0]
g = set(f[1:])
for i in range(1, n):
    f = x[i]
    g = g & set(f[1:])
print(len(g))
