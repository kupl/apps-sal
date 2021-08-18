import sys
def input(): return sys.stdin.readline().rstrip()


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
        i += 1
    return lower_divisors


def main():
    s, p = map(int, input().split())
    dev = make_divisors(p)
    for d in dev:
        if s - d == p // d:
            print("Yes")
            break
    else:
        print("No")


def __starting_point():
    main()


__starting_point()
