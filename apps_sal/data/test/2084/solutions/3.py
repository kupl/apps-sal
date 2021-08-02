n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
o = 0
for i in range(m):
    o += a[i]
print(o)
