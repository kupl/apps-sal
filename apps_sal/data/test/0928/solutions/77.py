import bisect

n, k = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

cul_sum = [0] * (n + 1)


# pre-processing
for i in range(1, n + 1):
    cul_sum[i] = cul_sum[i - 1] + A[i - 1]

ans = 0

for i in range(n + 1):
    target = k + cul_sum[i]
    right = bisect.bisect_left(cul_sum, target)
    if right == n + 1:
        break
    ans += n - (right - 1)

print(ans)
