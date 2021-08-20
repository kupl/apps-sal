(n, m, k) = map(int, input().split())
a = list(map(int, input().split()))
m -= 1
ml = mr = 10000000000
for i in range(m + 1, n):
    if a[i] != 0 and a[i] <= k:
        mr = i
        break
for i in range(m - 1, -1, -1):
    if a[i] != 0 and a[i] <= k:
        ml = i
        break
print(min(abs(m - ml), abs(m - mr)) * 10)
