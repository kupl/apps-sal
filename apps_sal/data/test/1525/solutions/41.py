h, w, k = list(map(int, input().split()))
dp = [0] * w
mod = 10 ** 9 + 7

comb = []
for bit in range(1 << w - 1):
    ok = True
    for j in range(w - 2):
        if bit >> j & 1 and bit >> j + 1 & 1:
            ok = False
    if ok:
        comb.append(bit)

dp[0] = 1
for i in range(h):
    next = [0] * w
    for bit in comb:
        moved = [False] * w
        for j in range(w):
            if bit >> j & 1:
                next[j + 1] += dp[j]
                next[j] += dp[j + 1]
                moved[j] = moved[j + 1] = True
            elif not moved[j]:
                next[j] += dp[j]
    dp = next
print((dp[k - 1] % mod))

