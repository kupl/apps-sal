l = [0] + [int(i) for i in input().split(" ")]

if l[13] == l[14] == l[15] == l[16] and \
    l[17] == l[18] == l[19] == l[20]:
    if l[5] == l[7] == l[10] == l[12] and \
        l[9] == l[11] == l[21] == l[23] and \
        l[1] == l[3] == l[6] == l[8] and \
        l[2] == l[4] == l[22] == l[24]:
        print('YES')
        return
    if l[5] == l[7] == l[2] == l[4] and \
        l[9] == l[11] == l[6] == l[8] and \
        l[1] == l[3] == l[21] == l[23] and \
        l[10] == l[12] == l[22] == l[24]:
        print('YES')
        return
if l[1] == l[2] == l[3] == l[4] and \
    l[9] == l[10] == l[11] == l[12]:
    if l[5] == l[6] == l[19] == l[20] and \
        l[17] == l[18] == l[23] == l[24] and \
        l[21] == l[22] == l[15] == l[16] and \
        l[13] == l[14] == l[7] == l[8]:
        print('YES')
        return
    if l[5] == l[6] == l[15] == l[16] and \
        l[13] == l[14] == l[23] == l[24] and \
        l[21] == l[22] == l[19] == l[20] and \
        l[17] == l[18] == l[7] == l[8]:
        print('YES')
        return
if l[5] == l[6] == l[7] == l[8] and \
    l[21] == l[22] == l[23] == l[24]:
    if l[3] == l[4] == l[18] == l[20] and \
        l[17] == l[19] == l[11] == l[12] and \
        l[9] == l[10] == l[13] == l[15] and \
        l[14] == l[16] == l[1] == l[2]:
        print('YES')
        return
    if l[3] == l[4] == l[13] == l[15] and \
        l[14] == l[16] == l[11] == l[12] and \
        l[9] == l[10] == l[18] == l[20] and \
        l[17] == l[19] == l[1] == l[2]:
        print('YES')
        return
print('NO')

