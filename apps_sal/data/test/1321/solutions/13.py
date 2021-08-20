hwarr = []
l = int(input())
for i in range(l):
    hwarr.append(list(map(int, input().split())))
pixs = ''
sws = sum((hwarr[n][0] for n in range(l)))
mhs = max((hwarr[n][1] for n in range(l)))
for i in range(l):
    if hwarr[i][1] == mhs:
        mi = i
        break
narr = []
narr += hwarr
narr.pop(mi)
nmhs = max((narr[n][1] for n in range(l - 1)))
for i in range(l):
    sw = sws - hwarr[i][0]
    if i == mi:
        mh = nmhs
    else:
        mh = mhs
    pixs += str(sw * mh) + ' '
print(pixs[:-1])
