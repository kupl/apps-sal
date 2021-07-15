N = int(input())
T = [int(input()) for _ in range(N)]

def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

res = T[0]
for t in T:
    gcd_ = gcd(res, t)
    res = res*t//gcd_
print(res)

