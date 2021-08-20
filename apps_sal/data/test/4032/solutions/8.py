(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
k1 = 0
k2 = 0
for i in range(n):
    if a[i] <= k:
        k1 += 1
    else:
        break
for i in range(n - 1, -1, -1):
    if a[i] <= k:
        k2 += 1
    else:
        break
print(min(k1 + k2, n))
