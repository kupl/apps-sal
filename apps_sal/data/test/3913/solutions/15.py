#python 3.5.2

n = int(input())
kataawal = input()

pos = []
posmuncul = []
muncul = set()
for i,x in zip(range(n),kataawal):
    if (x == '*'):
        pos.append(i)
    else:
        muncul.add(x)
        posmuncul.append(i)

m = int(input())
belum = []
for i in range(m):
    kata = input()
    yay = set()
    cancel = False
    for x in posmuncul:
        if (kata[x] != kataawal[x]):
            cancel = True
            break
            
    if (not cancel):
        for x in pos:
            if (kata[x] in muncul):
                cancel = True
                break
            else:
                yay.add(kata[x])

        if (not cancel):
            belum.append(yay)

if (len(belum) > 1):
    hoo = belum[0]
    for sett in belum[1:]:
        hoo = hoo.intersection(sett)
    print(len(hoo))
elif(len(belum) == 0):
    print(0)
else:
    print(len(belum[0]))
