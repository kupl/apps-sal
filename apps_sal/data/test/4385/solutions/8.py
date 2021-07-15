import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (*A,) = list(map(int, read().split()))
    k = A[-1]

    for i in range(5):
        for j in range(i + 1, 5):
            if A[j] - A[i] > k:
                print(':(')
                return

    print('Yay!')
    return


def __starting_point():
    main()

__starting_point()
