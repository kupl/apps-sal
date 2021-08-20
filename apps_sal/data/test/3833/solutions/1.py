s = input()
t = input()
overlap = t
tt = ''
for i in range(len(t) - 1):
    tt = tt + t[i]
    if t.endswith(tt):
        overlap = t[i + 1:]
zro = s.count('0')
mek = s.count('1')
zro_tum = t.count('0')
mek_tum = t.count('1')
zro_toxum = overlap.count('0')
mek_toxum = overlap.count('1')
if zro >= zro_tum and mek >= mek_tum:
    print(t, end='')
    zro -= zro_tum
    mek -= mek_tum
if zro_toxum:
    k = zro // zro_toxum
else:
    k = 10000000000
if mek_toxum:
    n = mek // mek_toxum
else:
    n = 10000000000
ans = min(n, k)
print(overlap * ans, end='')
zro -= zro_toxum * ans
mek -= mek_toxum * ans
print('0' * zro + '1' * mek)
