import sys
import queue


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)
MOD = 10 ** 9 + 7


def main():
    L = list(input())
    pow = [0] * (len(L) + 1)
    pow[0] = 1
    for i in range(1, len(L) + 1):
        pow[i] = pow[i - 1] * 3 % MOD
    N = len(L)
    if L[-1] == '0':
        answer = 1
    else:
        answer = 3
    for i in range(1, N):
        if L[N - i - 1] == '1':
            answer = answer * 2 + pow[i]
            answer %= MOD
        else:
            continue
    print(answer)


def __starting_point():
    main()


__starting_point()
