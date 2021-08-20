import sys
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (n, m) = list(map(int, input().split()))
    ABC = []
    for _ in range(m):
        (a, b) = list(map(int, input().split()))
        C = list(map(int, input().split()))
        bit = ['0'] * n
        for c in C:
            bit[c - 1] = '1'
        bit = ''.join(bit)
        ABC.append([a, b, int(bit, 2)])
    dp = [f_inf for _ in range(1 << n)]
    dp[0] = 0
    for i in range(1 << n):
        for (a, b, c) in ABC:
            idx = i | c
            dp[idx] = min(dp[idx], dp[i] + a)
    if dp[-1] != f_inf:
        print(dp[-1])
    else:
        print(-1)


def __starting_point():
    resolve()


__starting_point()
