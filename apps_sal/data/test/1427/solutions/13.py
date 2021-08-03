def main():
    from math import gcd
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline

    mod = 1000000007

    N = int(input())
    A = list(map(int, input().split()))

    lcm = 1
    for i in A:
        lcm = lcm * i // gcd(lcm, i)
    lcm %= mod

    ans = 0
    for i in A:
        ans += lcm * pow(i, mod - 2, mod)
        ans %= mod

    print(ans)


main()
