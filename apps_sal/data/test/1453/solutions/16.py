n, m = list(map(int, input().split()))
a = sorted(map(int, input().split()))
sums = [0] * n
ans = [0] * n
for i in range(m):
    sums[i] = ans[i] = a[i]
for i in range(m, n):
    sums[i] = sums[i - m] + a[i]
    ans[i] = ans[i - m] + sums[i]
for i in range(n - 1):
    ans[i + 1] += ans[i]
for i in reversed(list(range(m, n))):
    ans[i] -= ans[i - m]
print(*ans)

