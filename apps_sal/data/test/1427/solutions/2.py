n = int(input())
a = list(map(int, input().split()))

mod = 1000000007


def add(a, b):
    return (a + b) % mod


def mul(a, b):
    return (a * b) % mod


def pow(p, k):
    ret = 1
    b = p
    while k > 0:
        if k % 2 == 1:
            ret = mul(ret, b)
        b = mul(b, b)
        k //= 2
    return ret


def inv(p, k):
    return pow(p, mod - k - 1)


lcm = {}
ps = []
for i in range(n):
    ai = a[i]
    p = 2
    ps.append({})
    while ai > 1:
        if ai % p == 0:
            ps[i][p] = 0
            while ai % p == 0:
                ps[i][p] += 1
                ai //= p
            lcm[p] = max(lcm.get(p, 0), ps[i][p])
        p = p + 1 if p * p < ai else ai

lcmv = 1
for p in lcm:
    lcmv = mul(lcmv, pow(p, lcm[p]))

ret = 0
for i in range(n):
    prod = lcmv
    for p in ps[i]:
        prod = mul(prod, inv(p, ps[i][p]))
    ret = add(ret, prod)

print(ret)
