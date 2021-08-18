n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    a[i] = a[i] - 1

instack = [False] * n
processed = [False] * n
loopl = []
inloop = [False] * n


def dfs1(v):
    if (instack[v]):
        cl = 1
        t = a[v]
        inloop[v] = True
        while t != v:
            inloop[t] = True
            cl = cl + 1
            t = a[t]
        loopl.append(cl)
        return
    if processed[v]:
        return

    processed[v] = True
    instack[v] = True
    dfs1(a[v])
    instack[v] = False


for i in range(n):
    dfs1(i)
maxdis = 0
for i in range(n):
    t = i
    cl = 0
    while not inloop[t]:
        cl += 1
        t = a[t]
    maxdis = max(maxdis, cl)


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def mkd(a, b):
    return (a * b) // gcd(a, b)


mkl = 1
for i in loopl:
    mkl = mkd(mkl, i)
ans = mkl
while ans < maxdis:
    ans += mkl
print(ans)
