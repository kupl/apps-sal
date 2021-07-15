r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))
r4 = list(map(int, input().split()))
r5 = list(map(int, input().split()))
x = 0
y = 0
for cont in range(0,5):
    if r1[cont] == 1:
        x = cont
        y = 0
        break
    if r2[cont] == 1:
        x = cont
        y = 1
        break
    if r3[cont] == 1:
        x = cont
        y = 2
        break
    if r4[cont] == 1:
        x = cont
        y = 3
        break
    if r5[cont] == 1:
        x = cont
        y = 4
        break
ris = abs(y-2)+abs(x-2)
print(ris)
