import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (X, Y, A, B, C) = list(map(int, readline().split()))
    P = list(map(int, readline().split()))
    Q = list(map(int, readline().split()))
    R = list(map(int, readline().split()))
    P.sort(reverse=True)
    Q.sort(reverse=True)
    apple = P[:X] + Q[:Y] + R
    apple.sort(reverse=True)
    print(sum(apple[:X + Y]))
    return


def __starting_point():
    main()


__starting_point()
