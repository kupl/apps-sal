import sys


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def make_divisors(n: int):
    lower_divs = []
    upper_divs = []
    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            lower_divs.append(i)
            if i != n // i:
                upper_divs.append(n // i)
        i += 1
    return lower_divs + upper_divs[::-1]


def main():
    n = input_int()
    divs = make_divisors(n)
    ans = float('inf')
    for div in divs:
        a = div
        b = n // div
        if a * a <= n:
            ans = min(ans, max(len(str(a)), len(str(b))))
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
