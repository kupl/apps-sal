from itertools import permutations


def max2(x, y):
    return x if x > y else y


def solve(N, A, B):
    if A + B > N + 1:
        return None
    if A * B < N:
        return None
    res = [-1] * N
    rem = A
    i = 0
    while i + B + rem - 1 < N:
        rem -= 1
        o = i + B
        for k in range(B):
            res[i + k] = o - k - 1
        i += B
    p = N - i - rem + 1
    for k in range(p):
        res[i + k] = i + p - k - 1
    i += p
    rem -= 1
    for k in range(i, N):
        res[k] = k
    return res


def naive(N, A, B):
    for p in permutations(range(N)):
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if p[j] < p[i]:
                    dp[i] = max2(dp[i], dp[j] + 1)
        a = max(dp)
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if p[j] > p[i]:
                    dp[i] = max2(dp[i], dp[j] + 1)
        b = max(dp)
        if a == A and b == B:
            return p
    return None


def __starting_point():
    (N, A, B) = map(int, input().split())
    res = solve(N, A, B)
    if res is None:
        print(-1)
    else:
        print(*(v + 1 for v in res))


__starting_point()
