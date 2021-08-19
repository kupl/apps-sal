import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20


def I():
    return int(input())


def F():
    return float(input())


def S():
    return input()


def LI():
    return [int(x) for x in input().split()]


def LI_():
    return [int(x) - 1 for x in input().split()]


def LF():
    return [float(x) for x in input().split()]


def LS():
    return input().split()


def resolve():
    (N, K) = LI()
    RSP_score = LI()
    rsp_num = {'r': 0, 's': 1, 'p': 2}
    T = [rsp_num[i] for i in S()]
    dp = [[0] * 3 for _ in range(N)]
    for i in range(N):
        for j in range(3):
            if i - K >= 0:
                dp[i][j] += max([dp[i - K][k] for k in range(3) if k != j])
            if (j + 1) % 3 == T[i]:
                dp[i][j] += RSP_score[j]
    ans = sum([max(i) for i in dp[N - K:]])
    print(ans)


def __starting_point():
    resolve()


__starting_point()
