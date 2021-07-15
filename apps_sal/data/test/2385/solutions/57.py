import sys
sys.setrecursionlimit(1000000)


def input():
    return sys.stdin.readline()


n = int(input())
e = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = [int(i) - 1 for i in input().split()]
    e[a].append(b)
    e[b].append(a)

mod = 10**9+7

kkai = [1]
for i in range(1, 2*10 ** 5):
    kkai.append(kkai[-1] * i % mod)


def kai(x, p=mod):
    return kkai[x]


def comb(a, b, p=mod):
    if a < 0 or b < 0:
        return 0
    elif a < b:
        return 0
    if b == 0:
        return 1
    c = 1
    c *= kai(a, p)
    c *= pow(kai(b, p), p - 2, p)
    c *= pow(kai(a - b, p), p - 2, p)
    return c % p


child = [0] * n


def dfs1(i=0, r=-1):
    s = 1
    for j in e[i]:
        if j == r:
            continue
        s += dfs1(j, i)
    child[i] = s
    return s


dfs1()
a = [0] * n


def dfs2(i=0, r=-1):
    s = kai(child[i]-1)
    t = 1
    for j in e[i]:
        if j == r:
            continue
        s *= dfs2(j, i)
        s %= mod
        t *= kai(child[j])
        t %= mod
    s *= pow(t, mod - 2, mod)
    s %= mod
    a[i] = s
    return s


dfs2()
b = [0] * n


def dfs3(i=0, r=-1):
    if r == -1:
        b[i] = a[i]
    else:
        s = b[r] * child[i] % mod
        s *= pow(n-child[i], mod - 2, mod)
        s %= mod
        b[i] = s

    for j in e[i]:
        if j == r:
            continue
        dfs3(j, i)


dfs3()
print(("\n".join(map(str, b))))

