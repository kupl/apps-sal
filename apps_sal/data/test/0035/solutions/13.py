def re(a):
    if a == 'R':
        return 0
    elif a == 'B':
        return 1
    else:
        return 2


def llk(a):
    dd = ''.join(a)
    i = 0
    n = len(dd)
    su = 0
    while(i < n - 1):
        if dd[i] != dd[i + 1]:
            su += 1
        i += 1
    if su == 2:
        return 1
    else:
        return 0


a = [int(i) for i in input().split()]
k = []
lk = []
for i in range(a[0]):
    aa = input()
    k.append(aa)
    lk.append(set(aa))


ml = 0
ch = [0, 0, 0]
for i in k:
    if len(set(i)) == 1:
        ch[re(i[0])] += 1
    else:
        ml = 1
        break
mll = 0
gk = [''] * (a[1])
for i in range(a[0]):
    dk = k[i]
    for j in range(a[1]):
        gk[j] += (dk[j])
ch1 = [0, 0, 0]
for i in gk:
    if len(set(i)) == 1:
        ch1[re(i[0])] += 1
    else:
        mll = 1
        break


if (len(set(ch)) == 1 and ml == 0 and llk(k)):
    print("YES")
elif (len(set(ch1)) == 1 and mll == 0 and llk(gk)):
    print("YES")
else:
    print("NO")
