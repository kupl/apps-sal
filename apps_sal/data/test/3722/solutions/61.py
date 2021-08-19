import sys
import copy

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def fibo(x):
    MOD = 10 ** 9 + 7
    dp = [0] * (x + 10)

    dp[3] = 1
    dp[4] = 2

    for i in range(5, x + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= MOD

    return dp[x]


def main():
    N = int(input())
    CAA = input().strip()
    CAB = input().strip()
    CBA = input().strip()
    CBB = input().strip()

    MOD = 10 ** 9 + 7

    if N == 2:
        print((1))
        return

    if CAA == "A" and CAB == "A" and CBA == "A" and CBB == "A":
        print((1))
    elif CAA == "A" and CAB == "A" and CBA == "A" and CBB == "B":
        print((1))
    elif CAA == "A" and CAB == "A" and CBA == "B" and CBB == "A":
        print((1))
    elif CAA == "A" and CAB == "A" and CBA == "B" and CBB == "B":
        print((1))
    elif CAA == "A" and CAB == "B" and CBA == "A" and CBB == "A":
        print((pow(2, N - 3, MOD)))
    elif CAA == "A" and CAB == "B" and CBA == "A" and CBB == "B":
        print((1))
    elif CAA == "A" and CAB == "B" and CBA == "B" and CBB == "A":
        print((fibo(N)))
    elif CAA == "A" and CAB == "B" and CBA == "B" and CBB == "B":
        print((1))
    elif CAA == "B" and CAB == "A" and CBA == "A" and CBB == "A":
        print((fibo(N)))
    # fibo
    elif CAA == "B" and CAB == "A" and CBA == "A" and CBB == "B":
        print((fibo(N)))
    # fibo
    elif CAA == "B" and CAB == "A" and CBA == "B" and CBB == "A":
        print((pow(2, N - 3, MOD)))
    elif CAA == "B" and CAB == "A" and CBA == "B" and CBB == "B":
        print((pow(2, N - 3, MOD)))
    elif CAA == "B" and CAB == "B" and CBA == "A" and CBB == "A":
        print((pow(2, N - 3, MOD)))
    elif CAA == "B" and CAB == "B" and CBA == "A" and CBB == "B":
        print((1))
    elif CAA == "B" and CAB == "B" and CBA == "B" and CBB == "A":
        print((fibo(N)))
    # fibo
    elif CAA == "B" and CAB == "B" and CBA == "B" and CBB == "B":
        print((1))


def __starting_point():
    main()


__starting_point()
