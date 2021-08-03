def max_for_str(a, b):
    if len(a) > len(b):
        return a
    elif len(a) < len(b):
        return b
    else:  # This case is unlikely to happen.
        for c1, c2 in zip(a, b):
            if c1 > c2:
                return a
            elif c1 < c2:
                return b
        return a


match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

N, M = map(int, input().split())
As = list(input().split())

dp = [None] * (N + 1)
dp[0] = ""

for i in range(N + 1):
    for A in As:
        if i - match[int(A)] >= 0 and not dp[i - match[int(A)]] is None:
            if dp[i] is None:
                dp[i] = A + dp[i - match[int(A)]]
            else:
                dp[i] = max_for_str(dp[i], A + dp[i - match[int(A)]])

print(dp[N])
