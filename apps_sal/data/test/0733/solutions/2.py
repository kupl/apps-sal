(x, y, a, b) = list(map(int, input().split()))


def arch(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


c = x * y // arch(x, y)
print(b // c - (a - 1) // c)
