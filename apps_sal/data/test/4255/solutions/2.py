""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
(a, b, c) = list(map(int, input().split()))
print(a * b // 2)
