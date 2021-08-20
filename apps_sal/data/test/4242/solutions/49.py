from typing import Set


def divisors(n: int) -> Set[int]:
    divs = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
        i += 1
    return divs


def answer(a: int, b: int, k: int) -> int:
    divisors_a = divisors(a)
    divisors_b = divisors(b)
    common_divisors = list(divisors_a & divisors_b)
    common_divisors.sort()
    return common_divisors[-k]


def main():
    (a, b, k) = list(map(int, input().split()))
    print(answer(a, b, k))


def __starting_point():
    main()


__starting_point()
