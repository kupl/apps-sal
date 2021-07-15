n = int(input())
a = list(map(int,input().split()))
z = False
mi = 1
sc = 0
for i in a:
    if i == 0:
        z = True
        sc += 1
        continue
    sc += abs(i) - 1
    if(i < 0):
        mi *= -1
if mi == -1 and not z:
    sc += 2
print(sc)

