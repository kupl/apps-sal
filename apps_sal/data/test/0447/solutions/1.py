import sys

m, d = list(map(int, input().split()))
mod = 10**9 + 7


def solve(a: list):
    dp = [0] * m
    border = a[0] % m if a[0] != d else -1
    m10 = 10 % m

    for i in range(a[0]):
        if i != d:
            dp[i % m] += 1

    for i, digit in enumerate(a[1:], start=1):
        next_dp = [0] * m

        if i & 1:
            t = d % m
            for j in range(m):
                next_dp[t] += dp[j]
                t = t + m10 if t + m10 < m else t + m10 - m

            if border != -1:
                if d < digit:
                    next_dp[(border * 10 + d) % m] += 1
                    border = -1
                elif d == digit:
                    border = (border * 10 + d) % m
                else:
                    border = -1
        else:
            for j in range(m):
                if dp[j] == 0:
                    continue
                if dp[j] >= mod:
                    dp[j] -= mod

                t = (j * 10 - 1) % m
                for k in range(10):
                    t += 1
                    if t == m:
                        t = 0
                    if k == d:
                        continue
                    next_dp[t] += dp[j]
                    if next_dp[t] >= mod:
                        next_dp[t] -= mod

            if border != -1:
                for k in range(digit):
                    if k == d:
                        continue
                    next_dp[(border * 10 + k) % m] += 1
                if digit != d:
                    border = (border * 10 + digit) % m
                else:
                    border = -1

        dp = next_dp

    return dp[0] + (1 if border == 0 else 0)


a = list(map(int, input()))
b = list(map(int, input()))
a[-1] -= 1

for i in range(len(a) - 1, 0, -1):
    if a[i] < 0:
        a[i] = 9
        a[i - 1] -= 1
    else:
        break

ans = solve(b) - solve(a)
print(ans % mod)
