

""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10**9 + 7

s = input()
L = []

for i in range(len(s)):
    L.append(abs(int(s[i:i + 3]) - 753))
print((min(L)))
