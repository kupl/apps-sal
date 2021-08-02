N = int(input())
C_AA, C_AB, C_BA, C_BB = [input() for _ in range(4)]

if N <= 3:
    print((1))
    return

mod = 10**9 + 7


def solve(n):
    dp_a = [0] * (n + 1)
    dp_b = [0] * (n + 1)
    dp_b[0] = 1
    for i in range(1, n + 1):
        dp_b[i] = (dp_a[i - 1] + dp_b[i - 1]) % mod
        dp_a[i] = dp_b[i - 1]
    res = (dp_a[n] + dp_b[n]) % mod
    return res


if C_AB == "B":
    if C_BB == "B":
        ans = 1
    else:
        # [AB]xxxxxx[B]
        if C_BA == "B":
            # A は 1 連続まで
            ans = solve(N - 3)
        else:
            # B と A は任意
            ans = pow(2, N - 3, mod)
else:
    if C_AA == "A":
        ans = 1
    else:
        # [A]xxxxxx[AB]
        if C_BA == "A":
            ans = solve(N - 3)
        else:
            ans = pow(2, N - 3, mod)
print(ans)
