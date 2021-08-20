""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
n = int(input())
L = list(map(int, input().split()))
m = max(L)
L.remove(m)
s = sum(L)
if m < s:
    print('Yes')
else:
    print('No')
