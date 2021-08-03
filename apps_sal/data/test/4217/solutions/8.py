n, m = list(map(int, input().split()))

s = 0
for i in range(1, m + 1):
    s |= 1 << i


for i in range(n):
    a = list(map(int, input().split()))
    a = list(a)
    t = 0
    for j in range(1, len(a)):
        t |= 1 << a[j]
    s &= t


ans = 0
for i in range(1, m + 1):
    if (s & (1 << i)) != 0:
        ans += 1

print(ans)
