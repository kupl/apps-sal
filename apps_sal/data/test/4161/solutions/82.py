from math import gcd


def main():
    ans = 0
    k = int(input())
    for i in range(k):
        for j in range(k):
            for l in range(k):
                ans += gcd(i + 1, gcd(j + 1, l + 1))
    print(ans)


def __starting_point():
    main()


__starting_point()
