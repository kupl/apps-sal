from itertools import product
H, W, K = list(map(int, input().split()))
mod = 10 ** 9 + 7

if W == 1:
    print((1))
    return

up = [0] * W
right = [0] * W
left = [0] * W

for b in range(1 << (W - 1)):
    bridge = bin(b)[2:].zfill(W - 1)
    if "11" in bridge:
        continue

    # 左の棒
    if bridge[0] == "0":
        up[0] += 1
    else:
        right[0] += 1

    # 右の棒
    if bridge[-1] == "0":
        up[W - 1] += 1
    else:
        left[W - 1] += 1

    # 真ん中
    for i in range(1, W - 1):
        if bridge[i - 1] == "0" and bridge[i] == "1":
            right[i] += 1
        elif bridge[i - 1] == "1" and bridge[i] == "0":
            left[i] += 1
        else:
            up[i] += 1

up = [0] + up + [0]
right = [0] + right + [0]
left = [0] + left + [0]

dp = [0] * (W + 2)
dp[K] = 1
for _ in range(H):
    newDP = [0] * (W + 2)
    for i in range(1, W + 1):
        newDP[i] += dp[i - 1] * right[i - 1]
        newDP[i] += dp[i] * up[i]
        newDP[i] += dp[i + 1] * left[i + 1]
        newDP[i] %= mod
    dp = newDP

ans = dp[1]
print(ans)
