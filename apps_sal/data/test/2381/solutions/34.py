import sys
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    A = sorted(map(int, input().split()))
    mod = 10**9 + 7
    ans, sign = 1, 1

    l, r = 0, n - 1

    if k % 2:
        ans = A[r]
        r -= 1
        k -= 1
        if ans < 0:
            sign = -1
    while k:
        x = A[l] * A[l + 1]
        y = A[r] * A[r - 1]

        if x * sign > y * sign:
            ans = x % mod * ans % mod
            l += 2
        else:
            ans = y % mod * ans % mod
            r -= 2
        k -= 2
    print((ans + mod) % mod)


main()
