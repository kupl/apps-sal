s = input()
rub = 0
kop = 0
cur = 0
len_cur = 0
for i in range(len(s)):
    if 122 >= ord(s[i]) >= 97:
        if len_cur == 2:
            kop += cur - cur // 100 * 100
            rub += cur // 100
        else:
            rub += cur
        cur = 0
        len_cur = 0
    elif 57 >= ord(s[i]) >= 48:
        cur = 10 * cur + int(s[i])
        len_cur += 1
    elif s[i] == '.':
        len_cur = 0

if len_cur == 2:
    kop += cur - cur // 100 * 100
    rub += cur // 100
else:
    rub += cur

rub += kop // 100
kop = kop - kop // 100 * 100

if kop < 10:
    kop = '0' + str(kop)
kop = str(kop)
srub = ''
if len(str(rub)) % 3 != 0:
    srub += str(str(rub)[:len(str(rub)) % 3]) + '.'

c = 0
for i in range(len(str(rub)) % 3, len(str(rub))):
    c += 1
    srub += str(rub)[i]
    if c == 3:
        srub += '.'
        c = 0

if kop == '00':
    print(srub[:-1])
else:
    print(srub + kop)
