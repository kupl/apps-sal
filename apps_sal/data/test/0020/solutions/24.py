u = input().split(':')
h = u[0]
m = u[1]
def add(minute):
    hh = minute//60 + int(h)
    mm = minute%60 + int(m)
    if mm >= 60:
        mm -= 60
        hh += 1
    if hh >= 24:
        hh -= 24
    if hh < 10:
        hh = '0' + str(hh)
    else:
        hh = str(hh)
    if mm < 10:
        mm = '0' + str(mm)
    else:
        mm = str(mm)
    strr = hh + mm
    return strr == strr[::-1]

for i in range(0, 1000000):
    if add(i):
        print(i)
        break
    

