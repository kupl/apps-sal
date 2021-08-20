def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


(A, B, C, D) = map(int, input().split())


def div(x):
    num = x
    num -= x // C
    num -= x // D
    num += x // lcm(C, D)
    return num


print(div(B) - div(A - 1))
