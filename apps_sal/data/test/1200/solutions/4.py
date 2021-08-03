def gcd(a, b):
    if a == 0:
        return b
    while b:
        a %= b
        [a, b] = [b, a]
    return a


n = int(input())
a = [int(x) for x in input().split()]
a.sort()
tek = 0
res = 0
for x in a:
    if x != a[0]:
        res = gcd(res, x - tek)
    tek = x
print((tek - a[0]) // res - n + 1)
