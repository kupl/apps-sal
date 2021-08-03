n = int(input())
tmp = 2


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


for i in range(3, n + 1):
    tmp = tmp * i // gcd(tmp, i)

print(tmp + 1)
