from math import gcd


def solve(n):
    ans = n
    i = 2
    while i ** 2 <= n:
        if not n % i:
            while not n % i:
                n //= i
            ans -= ans // i
        i += 1
    if n > 1:
        ans -= ans // n
    return ans


def main():
    for _ in range(int(input())):
        a, m = list(map(int, input().split()))
        a = gcd(a, m)
        n = m // gcd(a, m)
        print(solve(m // gcd(a, m)))


main()

