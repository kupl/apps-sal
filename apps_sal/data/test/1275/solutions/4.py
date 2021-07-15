N, K = map(int, input().split())
tmp1, tmp2, ans = 0, 0, 0
for i in range(2, 2 * N + 1):
    tmp1 = min(i - 1, 2 * N + 1 - i)
    tmp2 = min(i - K - 1, 2 * N + 1 - i + K)
    if tmp1 >= 0 and tmp2 >= 0:
        ans += tmp1 * tmp2
print(ans)
