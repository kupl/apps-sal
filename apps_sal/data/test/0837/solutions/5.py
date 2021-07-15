n, a, b = input().split(' ')
n = int(n)
a = int(a)
b = int(b)
tk = tk2 = dk = dk2 = hg = hg2 = tag = tag2 = k1 = k2 = 0
kg = n
while kg >= 2:
    if kg % 2 != 0:
        tag = 1
        if tag == 1 and (kg-kg//2-1)*a < b:
            break
        hg2 = kg
        hg = (kg+1)//2
        while hg >= 2:
            if hg % 2 != 0:
                tag2 = 1
            if tag2 == 1 and (hg-hg//2-1)*a < b:
                break
            if tag2 == 0 and (hg-hg//2)*a < b:
                break
            if hg % 2 != 0:
                tk2 += 1
            hg //= 2
            tag2 = 0
            tk += 1
        t0 = b*tk + a*hg + a*tk2
        tag2 = 0
        hg = (hg2 - 1)//2
        while hg >= 2:
            if hg % 2 != 0:
                tag2 = 1
            if tag2 == 1 and (hg - hg//2 - 1) * a < b:
                break
            if tag2 == 0 and (hg - hg//2) * a < b:
                break
            if hg % 2 != 0:
                dk2 += 1
            hg //= 2
            tag2 = 0
            dk += 1
        t1 = b*dk + a*hg + a*dk2
        if t0 <= t1:
            kg += 1
        else:
            kg -= 1
        tk = tk2 = dk = dk2 = hg2 = 0
    if tag == 1:
        k2 += 1
    if (kg-kg//2)*a <= b:
        break
    kg //= 2
    tag = 0
    k1 += 1
t = b*k1 + k2*a + kg*a
print(t)

