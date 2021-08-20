"""a = int(input())
wow = input()

for i in wow:
    i = int(i)"""
wow = [int(e) for e in input()]
a1 = [wow[0], wow[1], wow[2]]
a2 = [wow[3], wow[4], wow[5]]
sum1 = sum(a1)
sum2 = sum(a2)
if sum1 == sum2:
    print(0)
else:
    if sum1 < sum2:
        noi = sum1
        mak = sum2
        fnoi = list(a1)
        fmak = list(a2)
        pontang = sum2 - sum1
    if sum2 < sum1:
        noi = sum2
        mak = sum1
        fnoi = list(a2)
        fmak = list(a1)
        pontang = sum1 - sum2
    fnoi.sort()
    fmak.sort()
    ptfnoi = [0] * 3
    ptfmak = [0] * 3
    'for i in range(3):\n        ptfnoi.append(9-fnoi[i])\n        ptfmak.append(fmak[i]-0)'
    ptfnoi[0] = 9 - fnoi[0]
    ptfnoi[1] = 9 - fnoi[1]
    ptfnoi[2] = 9 - fnoi[2]
    ptfmak[0] = fmak[0]
    ptfmak[1] = fmak[1]
    ptfmak[2] = fmak[2]
    'print(ptfnoi)\n    print(ptfmak)'
    lis = [ptfnoi[0], ptfnoi[1], ptfnoi[2], ptfmak[0], ptfmak[1], ptfmak[2]]
    lis.sort()
    mx1 = lis[5]
    mx2 = lis[4]
    if mx1 >= pontang:
        print(1)
    elif mx1 + mx2 >= pontang:
        print(2)
    else:
        print(3)
