h, n = list(map(int,input().split()))
a = list(map(int,input().split()))
hitpoint=h
atack = a[:]
for e in atack:
    hitpoint -= e
    if hitpoint <= 0:
        break
if hitpoint <= 0:
    print("Yes")
else:
    print("No")

