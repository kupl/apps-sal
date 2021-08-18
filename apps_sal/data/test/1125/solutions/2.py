import sys

N_MAX = 200000 + 5
INF = 10**9 + 7
sys.setrecursionlimit(N_MAX)
MOD = 10**9 + 7


def main():
    _ = int(sys.stdin.readline().rstrip())
    Arr = [int(x) for x in sys.stdin.readline().rstrip().split()]

    K = 43

    A = Arr[0]
    B = Arr[1]

    S = A + B
    X = 0
    for i in range(2, len(Arr)):
        X ^= Arr[i]

    dp = [[[-1 for x in [0, 1]] for _ in [0, 1]] for _ in range(K)]

    dp[0][0][0] = 0

    v = 1
    for i in range(K - 1):
        cx = X & 1
        cs = S & 1
        ca = A & 1
        for j in range(2):
            for k in range(2):
                if dp[i][j][k] == -1:
                    continue

                for na in range(2):
                    for nb in range(2):
                        ni = i + 1
                        nj = 0
                        nk = k
                        if na ^ nb != cx:
                            continue

                        ns = na + nb + j
                        if ns % 2 != cs:
                            continue

                        if ns >= 2:
                            nj = 1

                        if ca < na:
                            nk = 1
                        elif ca == na:
                            nk = k
                        else:
                            nk = 0

                        dp[ni][nj][nk] = max(dp[ni][nj][nk], dp[i][j][k] | (v * na))

        X >>= 1
        S >>= 1
        A >>= 1
        v <<= 1

    a = dp[K - 1][0][0]
    if a == -1 or a == 0:
        print((-1))
    else:
        print((Arr[0] - a))


main()
