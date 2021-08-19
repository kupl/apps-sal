n = int(input())
b = [0] * 8
a = [int(x) for x in input().split()]
for i in a:
    b[i] += 1
k1 = k2 = k3 = 0
if b[5] == b[7] == 0:
    if b[3] > 0:
        b[6] -= b[3]
        b[1] -= b[3]
        k2 = b[3]
        b[3] = 0
    if b[6] > 0:
        k1 = b[6]
        b[1] -= b[6]
        b[2] -= b[6]
        b[6] = 0
    if b[4] > 0:
        k3 = b[4]
        b[1] -= b[4]
        b[2] -= b[4]
        b[4] = 0
    if b[1] == b[2] == b[3] == b[4] == b[6] == 0:
        for i in range(k3):
            print('1 2 4')
        for i in range(k1):
            print('1 2 6')
        for i in range(k2):
            print('1 3 6')
    else:
        print('-1')
else:
    print('-1')
