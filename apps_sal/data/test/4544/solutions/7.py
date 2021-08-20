n = int(input())
a = [int(x) for x in input().split()]
a.sort()
p = [0] * (max(a) + 5)
for i in range(n):
    p[a[i] + 1] += 1
res = 0
for i in range(min(a), max(a) + 1):
    res = max(res, p[i] + p[i + 1] + p[i + 2])
print(res)
