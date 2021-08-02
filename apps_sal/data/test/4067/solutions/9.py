def mi():
    return list(map(int, input().split()))


'''
3
121
6
120110
6
211200
'''
n = int(input())
a = list(input())

zc, oc, tc = 0, 0, 0
for i in a:
    if i == '1':
        oc += 1
    elif i == '0':
        zc += 1
    else:
        tc += 1
if oc == tc and oc == zc:
    print(''.join(a))
    return
target = n // 3

ztba = max(0, target - zc)
ztbr = max(0, zc - target)

otba = max(0, target - oc)
otbr = max(0, oc - target)

ttba = max(0, target - tc)
ttbr = max(0, tc - target)

# print (target, ztba, ztbr, otba, otbr, ttba, ttbr)
if ztbr:
    for i in range(n - 1, -1, -1):
        if a[i] == '0':
            ztbr -= 1
            if ttba:
                a[i] = '2'
                ttba -= 1
            elif otba:
                a[i] = '1'
                otba -= 1
        if ztbr == 0:
            break
if otbr:
    if ztba:
        for i in range(n):
            if otbr == 0:
                break
            if a[i] == '1':
                a[i] = '0'
                otbr -= 1
                ztba -= 1
            if ztba == 0:
                break
    if otbr and ttba:
        for i in range(n - 1, -1, -1):
            if otbr == 0:
                break
            if a[i] == '1':
                a[i] = '2'
                otbr -= 1
                ttba -= 1
            if ttba == 0:
                break
if ttbr:
    if ztba:
        for i in range(n):
            if ttbr == 0:
                break
            if a[i] == '2':
                a[i] = '0'
                ttbr -= 1
                ztba -= 1
            if ztba == 0:
                break
    if ttbr and otba:
        for i in range(n):
            if ttbr == 0:
                break
            if a[i] == '2':
                a[i] = '1'
                ttbr -= 1
                otba -= 1
            if otba == 0:
                break
print(''.join(a))
