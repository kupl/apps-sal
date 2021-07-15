import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, T = list(map(int, readline().split()))

    ans = INF
    for _ in range(N):
        c, t = list(map(int, readline().split()))
        if t <= T and ans > c:
            ans = c
    
    if ans < INF:
        print(ans)
    else:
        print('TLE')
    return


def __starting_point():
    main()

__starting_point()
