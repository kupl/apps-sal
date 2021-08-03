def lcm(a):
    import math
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // math.gcd(x, a[i])
    return x


def resolve():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    print((lcm(T)))


resolve()
