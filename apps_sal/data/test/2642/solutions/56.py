import math
def main():
    N = int(input())
    d = {}
    za = zb = zab = r = 0
    mod = 10**9 + 7
    for i in range(N):
        a, b = list(map(int, input().split()))
        if a== 0 and b == 0:
            zab += 1
        elif b == 0:
            zb += 1
        elif a == 0:
            za += 1
        else:
            if a < 0:
                a, b = -a, -b
            x = math.gcd(abs(a), abs(b))
            d[(a//x, b//x)] = d.get((a//x, b//x), 0) + 1
    used = set()
    l = []
    for x in d:
        if x in used:
            continue
        a, b = x[0], x[1]
        used.add(x)
        if a * b > 0:
            t = (abs(b), -abs(a))
        else:
            t = (abs(b), abs(a))
        used.add(t)
        l.append((d[x], d.get(t, 0)))
    r = pow(2, za) + pow(2, zb) - 1
    for i in l:
        r *= (pow(2, i[0]) + pow(2, i[1]) - 1)
        r %= mod
    return (r - 1 + zab) % mod
print((main()))

