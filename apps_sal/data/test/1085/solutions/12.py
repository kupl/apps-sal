import sys


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_str_split(): return list(sys.stdin.readline().strip())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))


def divisors(num):
    lower = []
    upper = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            lower.append(i)
            if i * i != num:
                lower.append(num // i)
    return lower + upper[::-1]


def Main():
    n = read_int()
    div = divisors(n)[1:]
    ans = len(divisors(n - 1)) - 1
    for x in div:
        num = n
        while num % x == 0:
            num //= x
        if num % x == 1:
            ans += 1
    print(ans)


def __starting_point():
    Main()


__starting_point()
