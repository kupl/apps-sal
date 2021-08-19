d = {}
n = int(input())
for i in range(n):
    (x, y) = list(map(int, input().split()))
    if x in d:
        d[x] = max(d[x], y)
    else:
        d[x] = y
n = int(input())
for i in range(n):
    (x, y) = list(map(int, input().split()))
    if x in d:
        d[x] = max(d[x], y)
    else:
        d[x] = y
s = 0
for a in d:
    s += d[a]
print(s)
