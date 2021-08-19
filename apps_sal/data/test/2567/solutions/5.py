import sys
cases = True


def c2(n):
    return n * (n + 1) // 2


def get():
    return list(map(int, input().split()))


def bits(n: int):
    return list(bin(n)).count('1')


def main(test_case=False):
    n = int(input()) if test_case else 1
    for _ in range(n):
        test()


def flush():
    sys.stdout.flush()


def parr(arr):
    print(*arr, sep=' ')


def gcd(a, b):
    while b:
        if b % a == 0:
            break
        tmp = a
        a = b % a
        b = tmp
    return a


def test():
    n = int(input())
    s = input()
    c = s[n - 1]
    t = c * n
    print(t)


main(cases)
