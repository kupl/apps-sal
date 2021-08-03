def R(): return list(map(int, input().split()))


n, k = R()
a = R()
nch = 0
for i in a:
    if i % 2 == 1:
        nch += 1
ch = n - nch
c = n - k
c_dn = c // 2
c_st = c - c_dn

if c == 0:
    if nch % 2 == 1:
        print('Stannis')
    else:
        print('Daenerys')
elif c_dn >= nch:
    print('Daenerys')
else:
    if c_dn == c_st:
        if ch <= c_st and k % 2 == 1:
            print('Stannis')
        else:
            print('Daenerys')
    else:
        if c_dn >= ch and k % 2 == 0:
            print('Daenerys')
        else:
            print('Stannis')
