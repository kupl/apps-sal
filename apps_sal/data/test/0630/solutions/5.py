(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    ans[i] += min(n, i + 1 + k) - max(1, i + 1 - k) + 1
    if a[i] != 0:
        ans[i] += ans[a[i] - 1] - max(0, min(n, a[i] + k) - max(1, i + 1 - k) + 1)
print(*ans)
