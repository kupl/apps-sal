"""
Created on Thu Nov  2 13:36:10 2017

@author: savit
"""


def sum1(b):
    sum1 = 0
    for i in range(len(b)):
        sum1 += b[i][0]

    return sum1


n = int(input())
a = list(map(int, input().split()))
if(n != 2):
    do = True
    b = []
    min2 = min(a)
    for i in range(n):
        a[i] -= min2
        b.append([a[i], i])
    prin = []
    b.sort()
    prinx = -1
    if(sum(a) == 1 and min2 != 0):
        min2 -= 1
        for i in range(n):
            b[i][0] += 1
    if(sum1(b) % 2):
        if(b[-3][0] == 0):
            if(min2 == 0):

                do = False
            else:
                min2 -= 1
                for i in range(n):
                    b[i][0] += 1

        if(do):
            b[-1][0] -= 1
            b[-2][0] -= 1
            b[-3][0] -= 1
            prinx = (b[-1][1], b[-2][1], b[-3][1])
            b.sort()
    while(b[-1][0] != 0 and do):

        if(b[-2][0] == 0):
            if(min2 == 0):
                do = False
            else:
                min2 -= 1
                for i in range(n):
                    b[i][0] += 1
                if(sum1(b) % 2):
                    if(prinx == -1):
                        b[-1][0] -= 1
                        b[-2][0] -= 1
                        b[-3][0] -= 1
                        prinx = (b[-1][1], b[-2][1], b[-3][1])
                        b.sort()
                    else:
                        prin.append([prinx[0], prinx[1]])
                        prin.append([prinx[2], b[-1][1]])
                        b[-1][0] -= 1
                        prinx = -1

        b[-1][0] -= 1
        b[-2][0] -= 1
        prin.append([b[-1][1], b[-2][1]])
        b.sort()
    if(not do):
        while(b[-1][0] > 0):
            b[-1][0] -= 1
            prin.append([b[-1][1], b[-2][1]])

    x = [0 for i in range(n)]
    print(min2)

    if(prinx != -1):
        print(len(prin) + 1)
        x[prinx[0]] = 1
        x[prinx[1]] = 1
        x[prinx[2]] = 1
        print(*x, sep='')
        x[prinx[0]] = 0
        x[prinx[1]] = 0
        x[prinx[2]] = 0
    else:
        print(len(prin))

    for i in prin:
        x[i[0]] = 1
        x[i[1]] = 1
        print(*x, sep='')
        x[i[0]] = 0
        x[i[1]] = 0

else:
    if(a[1] == a[0]):
        print(a[0])
        print(0)
    else:
        print(0)
        print(max(a))
        for i in range(max(a)):
            print('11')
