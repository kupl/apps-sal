import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    s1 = input()
    s2 = input()
    P = []
    modulo = 10**9+7
    H, V = 0, 1
    for i in range(N):
        if i > 0 and s2[i] == s2[i-1]:
            P[-1] = H
        else:
            P.append(V)
    dp = []
    if P[0] == H:
        dp.append(6)
    else:
        dp.append(3)
    """
    A B     |C
    B A|C    A

    dp[i] = 3*dp[i-1] if P[i]=H&P[i-1]=H
            2*dp[i-1]    P[i]=H&P[i-1]=V
            2*dp[i-1]    P[i]=V&P[i-1]=V
            1*dp[i-1]    P[i]=V&P[i-1]=V
    """
    for i in range(1, len(P)):
        if P[i] == H and P[i-1] == H:
            dp.append(3*dp[i-1])
        elif P[i] == H and P[i-1] == V:
            dp.append(2*dp[i-1])
        elif P[i] == V and P[i-1] == V:
            dp.append(2*dp[i-1])
        else:
            dp.append(dp[i-1])
        dp[-1] %= modulo
    return dp[-1]


def __starting_point():
    print((solve()))

__starting_point()
