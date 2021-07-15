# coding: utf-8


def gcd(m, n):
    if n == 0: return m
    return gcd(n, m % n)

def main():
    A, B, C, D = list(map(int, input().split()))
    ans = B - A + 1
    ans -= B // C + B // D
    ans += (A - 1) // C + (A - 1) // D
    lcm = C // gcd(C, D) * D
    ans += B // lcm - (A - 1) // lcm
    print(ans)


def __starting_point():
    main()

__starting_point()
