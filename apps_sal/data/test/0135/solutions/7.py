def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a // gcd(a, b) * b


(n, k) = list(map(int, input().split()))
inf = 10 ** 18
x = 1
for i in range(1, k + 1):
    x = lcm(x, i)
    if x > inf:
        break
if x > inf or n % x != x - 1:
    print('No')
else:
    print('Yes')
