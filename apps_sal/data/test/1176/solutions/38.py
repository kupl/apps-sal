import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = list(map(int, read().split()))

    neg = total = 0
    min_abs = INF
    for a in A:
        if a < 0:
            neg += 1
        total += abs(a)
        if min_abs > abs(a):
            min_abs = abs(a)

    if neg % 2 == 1:
        total -= 2 * min_abs

    print(total)
    return


def __starting_point():
    main()

__starting_point()
