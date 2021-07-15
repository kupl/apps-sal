import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N, C = list(map(int, input().split()))
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    R = [[] for _ in range(3)]

    for i in range(N):
        for j in range(N):
            r = (i + 1) + (j + 1)
            if r % 3 == 0:
                R[0].append(c[i][j])
            elif r % 3 == 1:
                R[1].append(c[i][j])
            else:
                R[2].append(c[i][j])
    Diff = [[] for _ in range(3)]
    for i in range(3):
        l = len(R[i])

        for color in range(C):
            cnt = 0
            for j in range(l):
                cnt += D[R[i][j] - 1][color]
            Diff[i].append(cnt)
    answer = INF
    for i in range(C):
        for j in range(C):
            for k in range(C):
                if i == j or j == k or k == i:
                    continue
                else:
                    ans = Diff[0][i] + Diff[1][j] + Diff[2][k]
                    if ans < answer:
                        answer = ans
    print(answer)


def __starting_point():
    main()

__starting_point()
