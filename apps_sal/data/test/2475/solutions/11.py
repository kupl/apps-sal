import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    S = list(map(int, input().split()))

    ans = 0
    for C in range(1, N):
        n = N // C
        dp = [0] * n
        used = set([0])
        for k in range(1, n):
            A = N - 1 - k * C
            if A in used or k * C in used or A == k * C:
                break
            used.add(A)
            used.add(k * C)

            dp[k] = dp[k - 1] + S[A] + S[k * C]

        ans = max(ans, max(dp))

    return ans


def __starting_point():
    print((main()))


__starting_point()
