n, h, k = list(map(int, input().split()))
a = list(map(int, input().split()))
t = 0
l = 0
i = 0
while True:
    while i < n and h - l >= a[i]:
        l += a[i]
        i += 1
    if l <= k:
        t += 1
        l = 0
    t += l // k
    l %= k
    if i == n and l == 0:
        break
print(t)
