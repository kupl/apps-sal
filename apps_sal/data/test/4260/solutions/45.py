""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
(t, x) = list(map(int, input().split()))
print(t / x)
