import sys
in_file = sys.stdin
n = int(in_file.readline().strip())
Al = []
Ar = []
A = []
for _ in range(n):
    (x, y) = map(int, in_file.readline().strip().split())
    Al.append(x)
    Ar.append(y)
    A.append((x, y))
Al.sort()
Ar.sort()
A.sort()


def groups(L):
    p = L[0]
    G = [1]
    for i in range(1, len(L)):
        if p == L[i]:
            G[-1] += 1
        else:
            p = L[i]
            G.append(1)
    return G


def bin_exp(x, a, p):
    r = 1
    while a > 0:
        if a % 2 == 1:
            r = r * x % p
        x = x * x % p
        a = a // 2
    return r


def mod_fact(x, p):
    r = 1
    for i in range(1, x + 1):
        r = r * i % p
    return r


p = 998244353
Gl = groups(Al)
rl = 1
for i in Gl:
    rl = rl * mod_fact(i, p) % p
Gr = groups(Ar)
rr = 1
for i in Gr:
    rr = rr * mod_fact(i, p) % p
G = groups(A)
r = 1
for i in G:
    r = r * mod_fact(i, p) % p
if list(zip(Al, Ar)) != A:
    r = 0
res = (mod_fact(len(A), p) + r) % p
res = (p + res - rl) % p
res = (p + res - rr) % p
sys.stdout.write(str(res))
sys.stdout.flush()
