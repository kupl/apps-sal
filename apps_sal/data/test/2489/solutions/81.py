import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_A = max(A)
    dp = [True] * (max_A + 1)
    multi = [0] * (max_A + 1)
    for a in A:
        multi[a] += 1
        if multi[a] > 1:
            continue
        x = a
        while x + a <= max_A:
            x += a
            dp[x] = False
    ans = 0
    for a in A:
        if dp[a] and multi[a] == 1:
            ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
