from itertools import product

h, w, k = list(map(int, input().split()))
mod = 10 ** 9 + 7

dp = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(w + 1):
    dp[0][i] = 1 if i == 1 else 0


def check_valid_bridge(bridge):
    for i in range(1, w - 1):
        if bridge[i - 1] and bridge[i]:
            return False
    return True


for t in range(1, h + 1):
    for i in range(1, w + 1):
        X, Y, Z = 0, 0, 0
        if w != 1:
            p = product([True, False], repeat=w - 1)
            for bridge in p:
                if check_valid_bridge(bridge):
                    if i > 1 and bridge[i - 2]:
                        X += 1
                    elif i < w and bridge[i - 1]:
                        Y += 1
                    elif (i == 1 and not bridge[i - 1]) or (i == w and not bridge[i - 2]) or (1 < i < w and not bridge[i - 2] and not bridge[i - 1]):
                        Z += 1
        else:
            Z = 1
        pattern_1 = dp[t - 1][i - 1] * X if i > 1 else 0
        pattern_2 = dp[t - 1][i + 1] * Y if i < w else 0
        pattern_3 = dp[t - 1][i] * Z
        dp[t][i] = (pattern_1 + pattern_2 + pattern_3) % mod

print((dp[h][k]))
