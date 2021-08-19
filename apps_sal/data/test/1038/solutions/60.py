(a, b) = map(int, input().split())
'\n10**12 < 2**40\n任意の整数について、n ^ (n+1) = 1\n'


def f(n):
    if n % 2 != 0:
        if (n + 1) // 2 % 2 != 0:
            return 1
        else:
            return 0
    elif n // 2 % 2 != 0:
        return n ^ 1
    else:
        return n


print(f(a - 1) ^ f(b))
