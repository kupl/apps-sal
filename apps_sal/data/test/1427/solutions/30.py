n = int(input())
a = list(map(int, input().split()))
mod = 1000000007
lcm = {}
ps = []
for i in range(n):
    ai = a[i]
    p = 2
    ps.append({})
    while p * p <= ai:
        if ai % p == 0:
            ps[i][p] = 0
            while ai % p == 0:
                ps[i][p] += 1
                ai //= p
            lcm[p] = max(lcm.get(p, 0), ps[i][p])
        p += 1
    if ai > 1:
        ps[i][ai] = 1
        lcm[ai] = max(lcm.get(ai, 0), ps[i][ai])
lcmv = 1
for p in lcm:
    lcmv = lcmv * p ** lcm[p] % mod


def inv(p, k):
    k = mod - k - 1
    ret = 1
    b = p
    while k > 0:
        if k % 2 == 1:
            ret = ret * b % mod
        b = b * b % mod
        k //= 2
    return ret


ret = 0
for i in range(n):
    prod = lcmv
    for p in ps[i]:
        prod = prod * inv(p, ps[i][p]) % mod
    ret = (ret + prod) % mod
print(ret)
