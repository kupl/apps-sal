""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
(n, m) = list(map(int, input().split()))
L = [0] * (m + 1)
for i in range(n):
    A = list(map(int, input().split()))
    for k in range(1, A[0] + 1):
        L[A[k]] += 1
print(L.count(n))
