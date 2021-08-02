N, K = map(int, input().split())

mod = 998244353

lr = []
ans = [0] * (N + 1)
ans[1] = 1
lr = []
for _ in range(K):
    l, r = map(int, input().split())
    lr.append([l, r])

for i in range(2, N + 1):
    for l, r in lr:
        if i - l < 0:
            continue
        ans[i] += ans[i - l] - ans[max(0, i - r - 1)]
    ans[i] += ans[i - 1]
    ans[i] %= mod

print((ans[N] - ans[N - 1]) % mod)
