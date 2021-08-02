n, k = list(map(int, input().split()))
a = [int(i) for i in input().split()]
j = 0
s = 0
c = 0
for i in range(n):
    while j < n and s < k:
        s += a[j]
        j += 1
    if s >= k:
        c += n - j + 1
    s -= a[i]
print(c)
