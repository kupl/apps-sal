import functools

n, m = list(map(int, input().strip().split()))
x = list(map(int, input().strip().split()))
p = list(map(int, input().strip().split()))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


init = x[0]
for i in range(n):
    x[i] -= init

gcd_interval = functools.reduce(gcd, x)
for i in range(m):
    pi = p[i]
    if gcd_interval % pi == 0:
        print("YES")
        print(init, i + 1)
        return
print("NO")
