x = input().split()
n = int(x[0])
m = int(x[1])

l = input().split()
ans = 0
high = 0
for x in range(n):
    l[x] = int(l[x])
    y = l[x] // m
    if l[x] // m != l[x] / m:
        y += 1
    if y >= high:
        high = y
        ans = x + 1
print(ans)
