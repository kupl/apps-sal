n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
pSums = (n + 1) * [0]
pSums[0] = 0
for i in range(1, n + 1):
    pSums[i] = pSums[i - 1] + a[i - 1]

ans = 0
for i in range(m):
    l, r = list(map(int, input().split()))
    curSum = pSums[r] - pSums[l - 1]
    if curSum > 0:
        ans += curSum

print(ans)
