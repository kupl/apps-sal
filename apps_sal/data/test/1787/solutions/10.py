s = input()

l = []

c = 0

for i in s:
    if i == 'a':
        c += 1
    elif i == 'b':
        if c:
            l.append(c)
            c = 0

if c:
    l.append(c)

md = 10**9 + 7

ans = 0


d = {}


def inverse(a, n):
    if a in d:
        return d[a]
    t = 0
    t1 = 1
    r = n
    r1 = a
    while r1 > 0:
        q = r // r1
        tmp = t - q * t1
        t = t1
        t1 = tmp

        tmp = r - q * r1
        r = r1
        r1 = tmp

    if t < 0:
        t += n
    t = (t + n) % n
    d[a] = t
    return t


mul = 1
for i in l:
    mul *= i + 1
    mul %= md

for i in range(len(l)):
    mul = (mul * inverse(l[i] + 1, md)) % md
    m = mul * l[i]
    m %= md

    ans += m
    ans %= md

print(ans)
