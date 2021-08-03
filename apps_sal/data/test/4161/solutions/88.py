from math import gcd


def main():
    k = int(input())
    ans = 0
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            for k in range(1, k + 1):
                ans += gcd(gcd(i, j), k)
    print(ans)


def __starting_point():
    main()


__starting_point()
