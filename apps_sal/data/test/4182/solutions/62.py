import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, M, x, y) = list(map(int, readline().split()))
    X = list(map(int, readline().split()))
    Y = list(map(int, readline().split()))
    X.append(x)
    Y.append(y)
    if max(X) < min(Y):
        print('No War')
    else:
        print('War')
    return


def __starting_point():
    main()


__starting_point()
