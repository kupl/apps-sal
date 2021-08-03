n = int(input())
l = list(map(int, input().split()))
l.sort()
val = n // 2
x = 0
y = 0
for i in range(val):
    x += l[i]
for i in range(val, n):
    y += l[i]
print((x**2) + (y**2))
