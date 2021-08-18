

""" Definitions  """


def lcm(a, b):
    return a * b // math.gcd(a, b)


MOD = 10**9 + 7


n = int(input())
A = list(map(int, input().split()))
q = int(input())

L = [0] * (10**5 + 1)

for i in range(n):
    L[A[i]] += 1
s = sum(A)

for i in range(q):
    a, b = list(map(int, input().split()))
    s += (b - a) * L[a]
    L[b] += L[a]
    L[a] = 0
    print(s)
