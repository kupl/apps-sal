import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = list(map(int, read().split()))

    ans = 0
    right = 0
    s = 0

    for left in range(N):
        while right < N and s & A[right] == 0:
            s ^= A[right]
            right += 1

        ans += right - left

        if left == right:
            right += 1
        else:
            s ^= A[left]

    print(ans)
    return


def __starting_point():
    main()


__starting_point()
