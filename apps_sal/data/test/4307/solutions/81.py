import sys

input = sys.stdin.readline


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors


def main():
    N = int(input())

    ans = 0

    for i in range(1, N + 1):
        if i % 2 == 0:
            continue
        if len(make_divisors(i)) == 8:
            ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()
