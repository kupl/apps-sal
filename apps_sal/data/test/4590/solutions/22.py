(n, m, k) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
asum = [0]
bsum = [0]
for i in range(n):
    asum.append(asum[-1] + a[i])
for i in range(m):
    bsum.append(bsum[-1] + b[i])
ans = 0
for i in range(n + 1):
    if asum[i] > k:
        break
    while asum[i] + bsum[m] > k and m > 0:
        m -= 1
    ans = max(ans, i + m)
print(ans)
