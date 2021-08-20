def inputi():
    a = input().split(' ')
    return [int(i) for i in a]


(c1, c2, c3, c4) = inputi()
(n, m) = inputi()
a = inputi()
b = inputi()
sumn = 0
summ = 0
for i in a:
    if c1 * i < c2:
        sumn = sumn + c1 * i
    else:
        sumn = sumn + c2
if sumn > c3:
    sumn = c3
for i in b:
    if c1 * i < c2:
        summ = summ + c1 * i
    else:
        summ = summ + c2
if summ > c3:
    summ = c3
if sumn + summ > c4:
    print(c4)
else:
    print(sumn + summ)
