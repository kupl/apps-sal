ino = list(map(int, input().split()))
inos = list(map(int, input().split()))
n = ino[0] #фильтры
m = ino[1] #устройства
k = ino[2] #разетки
del ino
flag = False
#a = 1
for i in range(len(inos)):
        for j in range(len(inos) - 1, i, -1):
            #print(i)
            if inos[j] > inos[j-1]:
                inos[j], inos[j-1] = inos[j-1], inos[j]

if m <= k:
    print(0)
    flag = True
else:
    m = m - (k - 1)
    j = 0
    while(m > 0):
        if j != 0:
            m += 1
        m = m - inos[j]

        if j+1 == n and m != 0:
            print(-1)
            flag = True
            break
        j += 1
if flag == False:
    print(j)

"""
    while flag == False:
        for i in range(len(inos)):
            m = m - len(inos) + a - inos[a-1]

#for i in range(len(inos)):
#    print(inos[i])

#print(str(ino[0]), str(ino[1]), str(ino[2]))
"""
