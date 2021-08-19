import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    (n, m) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    L = [(1, 2), (2, 5), (3, 5), (4, 4), (5, 5), (6, 6), (7, 3), (8, 7), (9, 6)]
    B = []
    for (num, cost) in L:
        if num in A:
            B.append([num, cost])
    B.sort(key=lambda x: -x[0])
    dp = [-f_inf] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        for (_, cost) in B:
            if i - cost == 0:
                dp[i] = max(dp[i], dp[0] + 1)
            elif i - cost > 0 and dp[i - cost] != 0:
                dp[i] = max(dp[i], dp[i - cost] + 1)
    j = 0
    k = n
    res = ''
    while k > 0 and j < m:
        (num, cost) = B[j]
        if k - cost >= 0 and dp[k] - dp[k - cost] == 1:
            res += str(num)
            k -= cost
        else:
            j += 1
    print(res)


def __starting_point():
    resolve()


__starting_point()
