import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, *A) = list(map(int, read().split()))
    A = [list(map(int, f'{a:0>20b}')) for a in A]
    ans = 0
    right = 0
    digits = [0] * 20
    for left in range(N):
        while right < N and all((d + b <= 1 for (d, b) in zip(digits, A[right]))):
            for i in range(20):
                digits[i] += A[right][i]
            right += 1
        ans += right - left
        if left == right:
            right += 1
        else:
            for i in range(20):
                digits[i] -= A[left][i]
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
