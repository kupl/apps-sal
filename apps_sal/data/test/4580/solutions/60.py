n = int(input())
al = list(map(int, input().split()))
ratel = [0,0,0,0,0,0,0,0,0]

def check(a):
    if 1 <= a <= 399:
        return 0
    elif 400 <= a <= 799:
        return 1
    elif 800 <= a <= 1199:
        return 2
    elif 1200 <= a <= 1599:
        return 3
    elif 1600 <= a <= 1999:
        return 4
    elif 2000 <= a <= 2399:
        return 5
    elif 2400 <= a <= 2799:
        return 6
    elif 2800 <= a <= 3199:
        return 7
    else:
        return 8

for a in al:
    i = check(a)
    ratel[i] += 1


zeroc = 0
ratec = 0
for i in range(8):
    if ratel[i] == 0:
        zeroc += 1
    else:
        ratec += 1

if ratel[8] == 0:
    print(ratec,ratec)
elif 1 <= ratel[8] <= 8:
    if ratec == 0:
        print(1,ratel[8])
    elif ratel[8] < zeroc:
        print(ratec, ratec+ratel[8])
    elif ratel[8] >= zeroc:
        print(ratec,ratec+ratel[8])
else:
    if ratec == 0:
        print(1,ratel[8])
    else:
        print(ratec,ratec+ratel[8])
