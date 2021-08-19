""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
N = int(input())
ans = 0
P = []
for i in range(N):
    p = int(input())
    P.append(p)
    ans += p
ans -= max(P) // 2
print(ans)
