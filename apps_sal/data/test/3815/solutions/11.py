raw = input().split()
vals = [x for x in input()]
n,a,b,k = [int(x) for x in raw]
summ = 0
mod = 1000000009

def inv(x):
    return fast_power(x, mod-2)

def fast_power(a,n):
    ret = 1
    a = a % mod
    while n:
        if n&1:
            ret = ret*a%mod
        a = a*a%mod
        n >>= 1
    return ret

c = inv(a) * b % mod
cf = fast_power(c, k)
m = (n + 1) // k
if cf -1:
    p = (fast_power(cf, m) - 1) * inv(cf - 1) % mod
else:
    p = m
x = fast_power(a, n)
for i in range(k):
    summ = (summ + [-1, 1][vals[i] == '+'] * x * p) % mod
    x = (x * c) % mod

print(summ)

