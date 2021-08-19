""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
(y, m, d) = list(map(int, input().split('/')))
if y < 2019 or (y == 2019 and m <= 4):
    print('Heisei')
else:
    print('TBD')
