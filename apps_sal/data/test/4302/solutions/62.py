import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (A, B) = list(map(int, readline().split()))
    vec = [A, B, A - 1, B - 1]
    vec.sort(reverse=True)
    print(sum(vec[:2]))
    return


def __starting_point():
    main()


__starting_point()
