n = int(input())
a = list(map(int, input().split()))
dic = {a[0]: 1}
#board= ['*']*11
su = 1
kq = 1
for i in range(1, n):
    if dic.get(a[i], 0) == 0:
        dic.update({a[i]: 1})
    else:
        dic[a[i]] += 1
    su += 1
    cach = len(list(dic.keys()))
    c = 0
    c_ = 0
    for z in list(dic.keys()):
        if cach == 1:
            continue
        if cach == su:
            kq = su
            continue
        if dic[z] == (su - 1) / (cach - 1):
            c += 1
        if dic[z] == (su - 1) / cach:
            c_ += 1
    if c == cach - 1 or c_ == cach - 1:
        kq = su

print(kq)
