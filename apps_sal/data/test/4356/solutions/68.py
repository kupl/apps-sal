import sys

stdin = sys.stdin
sys.setrecursionlimit(10 ** 7)
MIN = -10 ** 9
MOD = 10 ** 9 + 7
INF = float("inf")
IINF = 10 ** 18


def solve():
    n, m = list(map(int, stdin.readline().rstrip().split()))
    a = [stdin.readline().rstrip() for _ in range(n)]
    b = [stdin.readline().rstrip() for _ in range(m)]

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            flag = True
            for h in range(m):
                if a[i + h][j:j + m] != b[h]:
                    flag = False
                    break
            if flag == True:
                print("Yes")
                return
    print("No")


def __starting_point():
    solve()


__starting_point()
