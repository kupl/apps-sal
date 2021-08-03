a, b = map(int, input().split())


def xor(n):
    m = n % 4
    if m == 0:
        return n
    elif m == 1:
        return 1
    elif m == 2:
        return n + 1
    else:
        return 0


print(xor(a - 1) ^ xor(b))
