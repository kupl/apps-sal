(n, k) = list(map(int, input().split(' ')))
mas = list(map(int, input().split(' ')))
di = dict()
res = 9999999999999999999999999999999999999
for i in mas:
    a = i * k
    a3 = str(a) + '_3'
    a2 = str(a) + '_2'
    s1 = str(i) + '_1'
    s2 = str(i) + '_2'
    s3 = str(i) + '_3'
    if di.get(s3):
        res += di.get(s3)
    if di.get(s2):
        if di.get(a3):
            di[a3] += di.get(s2)
        else:
            di[a3] = di.get(s2)
    if di.get(s1):
        if di.get(a2):
            di[a2] += 1
        else:
            di[a2] = 1
        di[s1] += 1
    else:
        if di.get(a2):
            di[a2] += 1
        else:
            di[a2] = 1
        di[s1] = 1
print(res - 9999999999999999999999999999999999999)
