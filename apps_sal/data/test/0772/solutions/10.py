import sys
inarray = []
outarray = [[1 for j in range(3)] for i in range(3)]
for i in range(3):
    k = [int(x) for x in sys.stdin.readline().split()]
    for j in range(3):
        if k[j] % 2 != 0:
            outarray[i][j] ^= 1
            if i - 1 >= 0:
                outarray[i - 1][j] ^= 1
            if j - 1 >= 0:
                outarray[i][j - 1] ^= 1
            if i + 1 < 3:
                outarray[i + 1][j] ^= 1
            if j + 1 < 3:
                outarray[i][j + 1] ^= 1
for i in range(3):
    print(''.join([str(x) for x in outarray[i]]))
