import sys


def check(q):
    if q[1] == q[2] == q[3] == q[4] and q[5] == q[6] == q[7] == q[8] and q[9] == q[10] == q[11] == q[12] and q[13] == q[14] == q[15] == q[16] and q[17] == q[18] == q[19] == q[20] and q[21] == q[22] == q[23] == q[24]:
        return True
    else:
        return False


a = [0] + [int(x) for x in input().split()]
swaps = []
b = a[:]
b[17] = a[3]
b[19] = a[4]
b[10] = a[17]
b[9] = a[19]
b[14] = a[9]
b[16] = a[10]
b[4] = a[14]
b[3] = a[16]
if check(b):
    print("YES")
    return
b = a[:]
b[17] = a[10]
b[19] = a[9]
b[10] = a[16]
b[9] = a[14]
b[14] = a[4]
b[16] = a[3]
b[4] = a[19]
b[3] = a[17]
if check(b):
    print("YES")
    return
b = a[:]
b[13] = a[21]
b[14] = a[22]
b[5] = a[13]
b[6] = a[14]
b[17] = a[5]
b[18] = a[6]
b[21] = a[17]
b[22] = a[18]
if check(b):
    print("YES")
    return
b = a[:]
b[21] = a[13]
b[22] = a[14]
b[13] = a[5]
b[14] = a[6]
b[5] = a[17]
b[6] = a[18]
b[17] = a[21]
b[18] = a[22]
if check(b):
    print("YES")
    return
b = a[:]
b[7] = a[19]
b[8] = a[20]
b[19] = a[23]
b[20] = a[24]
b[23] = a[15]
b[24] = a[16]
b[15] = a[7]
b[16] = a[8]
if check(b):
    print("YES")
    return
b = a[:]
b[19] = a[7]
b[20] = a[8]
b[23] = a[19]
b[24] = a[20]
b[15] = a[23]
b[16] = a[24]
b[7] = a[15]
b[8] = a[16]
if check(b):
    print("YES")
    return
b = a[:]
b[1] = a[5]
b[3] = a[7]
b[5] = a[9]
b[7] = a[11]
b[9] = a[22]
b[11] = a[24]
b[22] = a[1]
b[24] = a[3]
if check(b):
    print("YES")
    return
b = a[:]
b[5] = a[1]
b[7] = a[3]
b[9] = a[5]
b[11] = a[7]
b[22] = a[9]
b[24] = a[11]
b[1] = a[22]
b[3] = a[24]
if check(b):
    print("YES")
    return
b = a[:]
b[10] = a[6]
b[12] = a[8]
b[6] = a[2]
b[8] = a[4]
b[2] = a[23]
b[4] = a[21]
b[23] = a[10]
b[21] = a[12]
if check(b):
    print("YES")
    return
b = a[:]
b[6] = a[10]
b[8] = a[12]
b[2] = a[6]
b[4] = a[8]
b[23] = a[2]
b[21] = a[4]
b[10] = a[23]
b[12] = a[21]
if check(b):
    print("YES")
    return
b = a[:]
b[1] = a[18]
b[2] = a[20]
b[18] = a[12]
b[20] = a[11]
b[12] = a[15]
b[11] = a[13]
b[15] = a[1]
b[13] = a[2]
if check(b):
    print("YES")
    return
b = a[:]
b[18] = a[1]
b[20] = a[2]
b[12] = a[18]
b[11] = a[20]
b[15] = a[12]
b[13] = a[11]
b[1] = a[15]
b[2] = a[13]
if check(b):
    print("YES")
    return
print("NO")
