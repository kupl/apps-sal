import sys
input = sys.stdin.readline


def ins():
    return input().rstrip()


def ini():
    return int(input().rstrip())


def inm():
    return map(int, input().split())


def inl():
    return list(map(int, input().split()))


def out(x):
    return print('\n'.join(map(str, x)))


a = sorted(inl())
n = a[2] - a[1] + a[2] - a[0]
print((n + 2 - 1) // 2 + 1 if n % 2 else n // 2)
