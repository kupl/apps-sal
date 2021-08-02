n = int(input())
a = []; v = []; o = 0
a = list(map(int, input().split()))
for i in range(0, n + 1):
    v.append(0)
for i in range(n):
    v[a[i]] = i + 1
for i in range(1, n):
    o += abs(v[i] - v[i + 1])
print(o)
