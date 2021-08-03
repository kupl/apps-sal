n = int(input())
m = int(input())
k = 0
c = 0
o = 0
a = []
for i in range(n):
    k = int(input())
    a.append(k)
a.sort()
for i in range(n - 1, -1, -1):
    c += a[i]
    o += 1
    if c >= m:
        print(o)
        break
