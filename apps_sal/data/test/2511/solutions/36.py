import math
import sys
'\ndef p(n,r):\n    if n<r:\n        return 1\n    return math.factorial(n)//math.factorial(n-r)\n'


def main():
    input = sys.stdin.readline
    (N, K) = list(map(int, input().split()))
    E = [[] for _ in range(N)]
    MOD = 10 ** 9 + 7
    for _ in range(N - 1):
        (u, v) = list(map(int, input().split()))
        u -= 1
        v -= 1
        E[u].append(v)
        E[v].append(u)
    if N == 1:
        print(K)
        return
    color = [-1 for _ in range(N)]
    dp = [-1 for _ in range(N)]
    stack = []
    color[u] = 1
    ans = K
    for (i, v) in enumerate(E[u]):
        stack.append(v)
        ans *= K - i - 1
        ans %= MOD
    while stack:
        u = stack.pop()
        color[u] = 1
        length = 0
        for v in E[u]:
            if color[v] == -1:
                stack.append(v)
                length += 1
        if dp[length] == -1:
            tmp = 1
            for i in range(K - 1 - length, K - 1):
                tmp *= i
                tmp %= MOD
            ans *= tmp
        else:
            ans *= dp[length]
        ans %= MOD
    print(ans % MOD)


def __starting_point():
    main()


__starting_point()
