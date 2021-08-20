(a, b) = map(int, input().split())


def res(a, b):
    if a == 1:
        return b
    if b == 1:
        return a
    q = b // a
    b = b % a
    q += a // b
    return q + res(a % b, b)


print(res(a, b))
