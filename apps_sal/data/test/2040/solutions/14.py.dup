n = int(input())
prv = 0
r = [0] * 500
p = 0
for i in range(n):
    x = int(input())
    if x > p:
        d = x - p
        i = 0
        while d > 0:
            e = min(d, 9 - r[i])
            r[i] += e
            d -= e
            i += 1
    else:
        d = p - x + 1
        i = 0
        s = 0
        while d > s or r[i] == 9:
            s += r[i]
            i += 1
        j = 0
        d = s - d
        while j < i:
            e = min(d, 9)
            r[j] = e
            d -= e
            j += 1
        while r[i] == 9:
            i += 1
        r[i] += 1
    s = ''.join(map(str, reversed(r)))
    print(s.lstrip('0'))
    p = x
