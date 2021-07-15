a, b = list(map(int, input().split()))
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

(a, b) = (b, a) if a > b else (a, b)
c = b - a
if c == 0:
    print(0)
    return
pc = make_divisors(c)
ctr = a*b//(gcd(a, b))
ans = 0
for p in pc:
    ak = -(-a//p)*p
    k = ak - a
    bk = -(-b//p)*p
    lc = ak*bk//gcd(ak, bk)
    if ctr > lc:
        ctr = lc
        ans = k
print(ans)

