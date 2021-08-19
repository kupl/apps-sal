ino = list(map(int, input().split()))
inos = list(map(int, input().split()))
n = ino[0]
m = ino[1]
k = ino[2]
del ino
flag = False
for i in range(len(inos)):
    for j in range(len(inos) - 1, i, -1):
        if inos[j] > inos[j - 1]:
            (inos[j], inos[j - 1]) = (inos[j - 1], inos[j])
if m <= k:
    print(0)
    flag = True
else:
    m = m - (k - 1)
    j = 0
    while m > 0:
        if j != 0:
            m += 1
        m = m - inos[j]
        if j + 1 == n and m != 0:
            print(-1)
            flag = True
            break
        j += 1
if flag == False:
    print(j)
'\n    while flag == False:\n        for i in range(len(inos)):\n            m = m - len(inos) + a - inos[a-1]\n\n#for i in range(len(inos)):\n#    print(inos[i])\n\n#print(str(ino[0]), str(ino[1]), str(ino[2]))\n'
