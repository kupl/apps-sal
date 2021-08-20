MOD = 998244353


def getAns(a, b):
    if a < b:
        (a, b) = (b, a)
    s = 0
    total = 1
    for i in range(b + 1):
        s = s + total
        total = total * (a - i) // (i + 1) * (b - i)
    return s


x = [int(i) for i in input().split()]
x.sort()
print(getAns(x[2], x[1]) * getAns(x[1], x[0]) * getAns(x[2], x[0]) % MOD)
