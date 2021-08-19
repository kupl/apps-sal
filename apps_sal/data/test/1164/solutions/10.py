lat = 'qwertyuiopasdfghjklzxcvbnm'
lats = []
lats += lat
c = str(input())
for i in lats:
    c = c.replace(i, ' ')
c = c.split()
k = 0
for i in c:
    j = int(i.replace('.', ''))
    i = i.replace('.', ' ')
    i = i.split()
    if len(i[len(i) - 1]) != 2 or len(i) == 1:
        j *= 100
    k += j
print(format(k // 100, ',d').replace(',', '.'), end='')
if k % 100 != 0:
    print('.%02d' % (k % 100))
