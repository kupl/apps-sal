""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
(a, b) = list(map(int, input().split()))
if b % a == 0:
    print(a + b)
else:
    print(b - a)
