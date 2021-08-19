from math import gcd


def main():
    n = int(input())
    a = [int(c) for c in input().split()]
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    final = 0
    for i in range(1, int(g ** 0.5) + 1):
        if g % i == 0:
            if g // i != i:
                final += 2
            else:
                final += 1
    print(final)


main()
