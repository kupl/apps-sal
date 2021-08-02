'''

0  |  a1       a2         a3
1  |  a1       a1+a2      a1+ a2+a3
2  |  a1      2a1+a2     3a1+2a2+a3
...      ...        ...
cada celda depende de la izq y la superior, es como numeros
combinatorios, el a1 es triang(k) en 3, y los inmediatamente anteriores
por k (con k=0 es perm original!)
'''
n, k = list(map(int, input().split(" ")))
l = list(map(int, input().split(" ")))

v = []
for x in l:
    if x != 0 or v:
        v.append(x)


def bruteforce(v, k):
    ret = 0
    while True:
        accm = 0
        for i in range(len(v)):
            if v[i] >= k: return ret
            accm += v[i]
            v[i] = accm
        ret += 1
    return ret


def smarty(v, k):
    def triang(x):
        return x * (x + 1) // 2
    l, r = 0, 10**18
    ans = 10**18
    while l <= r:
        h = (l + r) // 2
        f0 = v[0]
        f1 = h * v[0] + v[1]
        f2 = triang(h) * v[0] + h * v[1] + v[0] if n == 3 else 0
        if max(f0, f1, f2) >= k:
            r = h - 1
            ans = min(ans, h)
        else:
            l = h + 1
    return ans


n = len(v)
if n > 3:
    print(bruteforce(v, k))
else:
    print(smarty(v, k))
