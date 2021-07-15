from fractions import gcd
tot = 0

t = []
a = int(input())
for i in range(a):
    x, y = list(map(int, input().split(' ')))
    t.append([x,y])


for i in t:
    slope = {}
    zd = 0
    oded = []
    for j in t:
        if j != i:
            if j[0] == i[0]:
                zd += 1
            else:
                f1 = (j[1]-i[1])
                f2 = (j[0]-i[0])
                gd = gcd(f1, f2)
                if gd == 0:
                    oded.append(987987987)
                
                else:
                    f1 //= gd
                    f2 //= gd
                    kk = f1*10000+f2
                    oded.append(kk)
    oded.sort()
    oded.append(-1000000)
    asdf = 0
    kk = [-1] + [ea for ea in range(len(oded)-1) if oded[ea] != oded[ea+1]]
    kk2 = [kk[i+1] - kk[i] for i in range(len(kk)-1)]

    for ii in kk2:
        tot += (ii*(ii-1)//2)
    tot+=(zd*(zd-1)//2)

tot //= 3
print(int(a*(a-1)*(a-2)//6-tot))

