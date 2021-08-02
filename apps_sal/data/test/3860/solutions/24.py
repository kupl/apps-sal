def gcd(x, y):
    if(y == 0):
        return x
    return gcd(y, x % y)


b = int(input())
g = int(input())
n = int(input())
mb = max(0, n - g)
mg = max(0, n - b)
mab = min(n, b)
mag = min(n, g)
cb = mab - mb
cg = mag - mg
print(min([cb + 1, cg + 1, n + 1]))
