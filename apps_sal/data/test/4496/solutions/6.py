""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
D = int(input())
L = ['Christmas Eve', 'Christmas', 'Christmas Eve Eve Eve', 'Christmas Eve Eve']
print(L[D % 4])
