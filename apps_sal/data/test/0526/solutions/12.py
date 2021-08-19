(n, m) = tuple(map(int, input().strip().split()))
mat = []
for i in range(n):
    mmm = list(map(int, input().strip().split()))
    mat.append(mmm)
st = 0
rnum = -1
cnum = -1
for i in range(n):
    for ii in range(m - 1):
        if mat[i][ii] != mat[i][ii + 1]:
            st = 1
            rnum = i
            cnum = ii
            break
    if st == 1:
        break
if not st or m == 1:
    hh = 0
    sr = ''
    for i in range(n):
        hh = hh ^ mat[i][0]
        sr = sr + str(1) + ' '
    if hh == 0:
        print('NIE')
    else:
        print('TAK')
        print(sr)
else:
    print('TAK')
    sr = ''
    hh = 0
    for i in range(0, n):
        if i != rnum:
            hh = hh ^ mat[i][0]
    if hh ^ mat[rnum][cnum] == 0:
        for i in range(0, n):
            if i != rnum:
                sr = sr + str(1) + ' '
            else:
                sr = sr + str(cnum + 2) + ' '
    else:
        for i in range(0, n):
            if i != rnum:
                sr = sr + str(1) + ' '
            else:
                sr = sr + str(cnum + 1) + ' '
    print(sr)
