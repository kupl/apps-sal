""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10 ** 9 + 7
(k, n) = list(map(int, input().split()))
A = list(map(int, input().split()))
m = 2 * 10 ** 5
M = [0] * n
dist = min(A[n - 1] - A[0], k - A[n - 1] + A[0])
for i in range(n - 1):
    dist = max(dist, A[i + 1] - A[i])
print(k - dist)
