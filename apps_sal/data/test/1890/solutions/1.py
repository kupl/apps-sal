mod = 1000000007

def egcd(a, b):
    d = a
    if b != 0:
        d, y, x = egcd(b, a%b)
        y -= (a // b) * x
        return d, x, y
    else:
        return a, 1, 0

def inv(a, m):
    d, x, y = egcd(a, m)
    return (m+x%m)%m


a = input()
k = int(input())
t = len(a)
d = 0
for i, c in enumerate(a):
    if not int(c) % 5:
        d += pow(2, i, mod)
        d %= mod
d %= mod
print(d*(pow(2, k*t, mod)-1)*inv((pow(2, t, mod)-1)%mod, mod)%mod)

