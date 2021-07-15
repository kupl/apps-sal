def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, K = ZZ()
    A = ZZ()
    if K == 0:
        print((sum(A)))
        return

    bK = format(K, 'b')
    msb = len(bK)
    plus = [0] * msb

    for a in A:
        for i, b in enumerate(format(a, '0{}b'.format(msb))[::-1][:msb]): plus[i] += int(b)
    e = 1
    for i in range(msb):
        plus[i] = e * (N - 2 * plus[i])
        e *= 2

    dp = [[0] * 2 for _ in range(msb)]
    dp[0][0] = plus[i]
    plus = plus[::-1]

    for i in range(msb-1):
        dp[i+1][0] = max(dp[i+1][0], dp[i][0] + plus[i+1] * int(bK[i+1]))
        if int(bK[i+1]) == 1: dp[i+1][1] = max(dp[i+1][1], dp[i][0])
        dp[i+1][1] = max(dp[i+1][1], dp[i][1], dp[i][1] + plus[i+1])
    print((max(dp[msb-1]) + sum(A)))

    return

def __starting_point():
    main()

__starting_point()
