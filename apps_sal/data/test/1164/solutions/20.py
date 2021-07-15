s = input()
ms = ['']
dct = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
p = 0
for i in s:
    if i in dct:
        ms[-1] += i
        p = 1
    else:
        if p:
            ms.append('')
            p = 0
rub = 0
kop = 0
if ms[0] == '':
    ms = []
for i in ms:
    box = i.split('.')
    l = len(box)
    a = 0
    b = 0
    p = 0
    for j in range(l - 1, -1, -1):
        if len(box[j]) == 2 and j == l - 1:
            b = int(box[j])
            p = 1
        else:
            a += int(box[j]) * (1000 ** (l - 1 - j - p))
    rub += a
    kop += b
rub += kop // 100
kop %= 100

s = str(rub)
l = len(s)
d = l % 3
ret = ''
ind = 0
if d:
    ind = d
    for i in range(d):
        ret += s[i]
    ret += '.'
cnt = 0
for i in range(ind, l):
    ret += s[i]
    cnt += 1
    cnt %= 3
    if not cnt:
        ret += '.'
if kop:
    if kop < 10:
        ret += '0'
    ret += str(kop)
    print(ret)
else:
    l = len(ret)
    for i in range(0, l - 1, 1):
        print(ret[i], end = '')

    
    
            
        
