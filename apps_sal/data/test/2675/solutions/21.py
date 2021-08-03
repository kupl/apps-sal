n, m = map(int, input().split())
x = {}
y = {}
for i in range(n):
    p, s = map(int, input().split())
    if p * s in x:
        x[p * s] += 1
    else:
        x[p * s] = 1
for i in range(m):
    p, s = map(int, input().split())
    if p * s in y:
        y[p * s] += 1
    else:
        y[p * s] = 1
c = 0
for i in x:
    if i in y:
        c += min(x[i], y[i])
print(c)
