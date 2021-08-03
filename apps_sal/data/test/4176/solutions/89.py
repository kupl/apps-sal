A, B = map(int, input().split())


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def abc(a, b):
    return(a * b // gcd(a, b))


print(abc(A, B))
