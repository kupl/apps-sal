c = [0] + list(map(int, input().split()))
ans = False
if c[1] == c[2] == c[17] == c[19] and \
    c[18] == c[20] == c[9] == c[10] and \
    c[11] == c[12] == c[14] == c[16] and \
    c[13] == c[15] == c[3] == c[4] and \
    c[21] == c[22] == c[23] == c[24] and \
    c[5] == c[6] == c[7] == c[8]:
    ans = True
elif c[1] == c[2] == c[14] == c[16] and \
    c[18] == c[20] == c[3] == c[4] and \
    c[11] == c[12] == c[17] == c[19] and \
    c[13] == c[15] == c[9] == c[10] and \
    c[21] == c[22] == c[23] == c[24] and \
    c[5] == c[6] == c[7] == c[8]:
    ans = True
elif c[21] == c[22] == c[15] == c[16] and \
    c[13] == c[14] == c[7] == c[8] and \
    c[5] == c[6] == c[19] == c[20] and \
    c[17] == c[18] == c[23] == c[24] and \
    c[1] == c[2] == c[3] == c[4] and \
    c[9] == c[10] == c[11] == c[12]:
    ans = True
elif c[21] == c[22] == c[19] == c[20] and \
    c[13] == c[14] == c[23] == c[24] and \
    c[5] == c[6] == c[15] == c[16] and \
    c[17] == c[18] == c[7] == c[8] and \
    c[1] == c[2] == c[3] == c[4] and \
    c[9] == c[10] == c[11] == c[12]:
    ans = True
elif c[21] == c[23] == c[1] == c[3] and \
    c[2] == c[4] == c[5] == c[7] and \
    c[6] == c[8] == c[9] == c[11] and \
    c[10] == c[12] == c[22] == c[24] and \
    c[13] == c[14] == c[15] == c[16] and \
    c[17] == c[18] == c[19] == c[20]:
    ans = True
elif c[21] == c[23] == c[9] == c[11] and \
    c[2] == c[4] == c[22] == c[24] and \
    c[6] == c[8] == c[1] == c[3] and \
    c[10] == c[12] == c[5] == c[7] and \
    c[13] == c[14] == c[15] == c[16] and \
    c[17] == c[18] == c[19] == c[20]:
    ans = True
print('YES' if ans else 'NO')


