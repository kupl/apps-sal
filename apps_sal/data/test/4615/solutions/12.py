a, b, c, d, e, f = map(int, input().split())

max_s = 0
max_w = a
max_conc = 0

water_s = set()
sugar_s = set()
for i in range(f // a // 100 + 1):
    aa = a * i
    for j in range(f // b // 100 + 1):
        bb = b * j
        if aa + bb <= f // 100:
            water_s.add(aa + bb)

for i in range(f // c + 1):
    cc = c * i
    for j in range(f // d + 1):
        dd = d * j
        if cc + dd <= f:
            sugar_s.add(cc + dd)

for w in water_s:
    for sg in sugar_s:
        if w * 100 + sg <= f and w * e >= sg and w + sg > 0:
            conc = (100 * sg) / (100 * w + sg)
            if max_conc < conc:
                max_conc = conc
                max_w = w
                max_s = sg
print(max_w * 100 + max_s, max_s)
