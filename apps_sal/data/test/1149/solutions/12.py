nstr = input()
n = int(nstr)
pstr = input()
aa = pstr.split(' ')
a = aa[1:]
qstr = input()
bb = qstr.split(' ')
b = bb[1:]
for i in a:
    i = int(i)
for i in b:
    i = int(i)
f = 0
for i in range(1, n + 1):
    if str(i) in a or str(i) in b:
        continue
    else:
        f = 1
        print('Oh, my keyboard!')
        break
if f == 0:
    print('I become the guy.')
