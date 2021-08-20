l = input().split(' ')
H = int(l[0])
W = int(l[1])
K = int(l[2])
c = []
retval = 0
for i in range(H):
    c.append(input())
for maski in range(1 << H):
    for maskj in range(1 << W):
        count = 0
        for i in range(H):
            for j in range(W):
                if maski >> i & 1 == 1 and maskj >> j & 1 == 1 and (c[i][j] == '#'):
                    count += 1
        if count == K:
            retval += 1
print(retval)
