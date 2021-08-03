n = int(input())
s1 = input()
s2 = input()
s3 = input()

k = len(s1)

ss = []

ss.append(sorted(s1))
ss.append(sorted(s2))
ss.append(sorted(s3))

mm = [0] * 3

for i in range(3):
    mmi = 1
    ssi = ss[i]
    for j in range(k - 1):
        if ssi[j] == ssi[j + 1]:
            mmi = mmi + 1
        else:
            mmi = 1
        if mmi > mm[i]:
            mm[i] = mmi

if n == 1:
    for i in range(3):
        if mm[i] == k:
            mm[i] = k - 1
        else:
            mm[i] = mm[i] + n
            if mm[i] > k:
                mm[i] = k
else:
    for i in range(3):
        mm[i] = mm[i] + n
        if mm[i] > k:
            mm[i] = k

mmm = max(mm)
mmn = 0

for i in range(3):
    if mmm == mm[i]:
        mmn = mmn + 1

if mmn > 1:
    print('Draw')
else:
    ind = mm.index(mmm)
    print(['Kuro', 'Shiro', 'Katie'][ind])
