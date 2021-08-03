MOD = 10**9 + 7


def pow(x, n, MOD):
    if(n == 0):
        return 1
    if(n % 2 == 0):
        a = pow(x, n // 2, MOD)
        return a * a % MOD
    else:
        a = pow(x, n // 2, MOD)
        return (x * a * a) % MOD


n, x = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
s = sum(a)
d = []

for el in a:
    d.append(s - el)

d.sort()
i = 0
gcd = d[0]
c = 0
while i < n and d[i] == gcd:
    c += 1
    i += 1

while c % x == 0:
    c = c // x
    gcd += 1

    while i < n and d[i] == gcd:
        c += 1
        i += 1

if gcd > s:
    gcd = s

print(pow(x, gcd, MOD))
