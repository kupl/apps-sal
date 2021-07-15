N, *AB = map(int, open(0).read().split())
AB = list(zip(*[iter(AB)] * 2))

memo = [False] * (2 * N + 1)
for i, (a, b) in enumerate(AB):
    if (a != -1 and memo[a] or b != -1 and memo[b] or
        a != -1 and b != -1 and a > b):
        print("No")
        return

    if a != -1:
        memo[a] = True
    if b != -1:
        memo[b] = True

dp = [True] + [False] * N
for i in range(N):
    if not dp[i]:
        continue

    for j in range(1, N - i + 1):
        if dp[i + j]:
            continue

        ok = True
        for a, b in AB:
            if not ok:
                break

            in_a = (2 * i + 1 <= a <= 2 * i + j)
            in_b = (2 * i + j + 1 <= b <= 2 * i + 2 * j)
            if a != -1 and b != -1 and (in_a ^ in_b) or in_a and in_b and b - a != j:
                ok = False

            if a != -1 and 2 * i + j + 1 <= a <= 2 * i + 2 * j or in_a and b - a != j and memo[a + j]:
                ok = False

            if b != -1 and 2 * i + 1 <= b <= 2 * i + j or in_b and b - a != j and memo[b - j]:
                ok = False

        dp[i + j] = ok

if dp[N]:
    print("Yes")
else:
    print("No")
