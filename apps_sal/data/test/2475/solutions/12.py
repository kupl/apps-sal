import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for C in range(1, N // 2):
        n = (N - 1) // C
        point = 0
        for k in range(1, n):
            A = N - 1 - k * C
            if A < C or ((N - 1) % C == 0 and A <= k * C):
                break
            point += S[A] + S[k * C]
            ans = max(ans, point)
    return ans


def __starting_point():
    print(main())


__starting_point()
