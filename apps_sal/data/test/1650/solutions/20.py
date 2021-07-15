L = input()
l = len(L)
mod = 10**9 + 7
ans = 1  # (0,0)

d = dict()


def modpow(x, n, mod):
    if x not in d:
        d[x] = [1]
    l = len(d[x])
    ret = d[x][-1]
    for i in range(l, n+1):
        ret *= x
        ret %= mod
        d[x].append(ret)
    return(d[x][n])


ans = modpow(3, l, mod)

r = 0
count = 0

for i in range(l):
    if L[i] == '0':
        r = modpow(3, l-i-1, mod) * modpow(2, count, mod) * 2
        ans -= r
        ans %= mod
    else:
        count += 1
print(ans)

