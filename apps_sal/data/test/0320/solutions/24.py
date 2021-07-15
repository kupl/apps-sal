n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split(' '))))
Summ1=Summ2=0
for i in range(n):
    Summ1+=a[i][0]
    Summ2+=a[i][1]
F = False

if Summ1//2 == Summ1/2 and Summ2//2 == Summ2/2:
    print(0)
    F = True

if Summ1//2 != Summ1/2 and Summ2//2 != Summ2/2 and n!=1:
    for i in range(n):
        if (a[i][1]//2!=a[i][1]/2 and a[i][0]//2==a[i][0]/2) or (a[i][0]//2!=a[i][0]/2 and a[i][1]//2==a[i][1]/2):
            print(1)
            F = True
            break
if F == False:
    print(-1)
