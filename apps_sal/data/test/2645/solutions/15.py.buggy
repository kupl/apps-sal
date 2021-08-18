from math import ceil
s = input()
gu = s.count('g')
pa = s.count('p')

p = len(s) // 2
g = int(ceil(len(s) / 2))

gu, g = gu - min(gu, g), g - min(gu, g)
pa, p = pa - min(pa, p), p - min(pa, p)

if g == 0 and gu == 0 and p == 0 and pa == 0:
    print(0)
    return

if p == 0 and gu == 0:
    print(-g)
    return

if pa == 0 and g == 0:
    print(gu)
    return
