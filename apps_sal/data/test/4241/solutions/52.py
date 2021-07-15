import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    S = input()
    T = input()
    answer = INF
    for i in range(len(S) - len(T) + 1):
        tmp = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                tmp += 1
        answer = min(answer, tmp)
    print(answer)


def __starting_point():
    main()

__starting_point()
