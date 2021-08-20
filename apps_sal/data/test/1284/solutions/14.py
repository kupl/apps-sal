n = int(input())
l = list(map(int, input().split()))
s = sum(l)
x = 0
k = n // 2
for i in range(k):
    x += l[i * 2]
minx = x
for i in range(n - 1):
    x -= l[i * 2 % n]
    x += l[(k + i) * 2 % n]
    minx = min(minx, x)
print(s - minx)
