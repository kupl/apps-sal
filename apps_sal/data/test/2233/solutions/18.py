import re

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    difa = []
    difb = []
    diffS = 0
    for i in range(0, n):
        if(a[i] == b[i]):
            continue
        difa += [a[i]]
        difb += [b[i]]
        diffS += 1
        if(diffS > 2):
            break
    if(diffS < 2 or diffS > 2):
        print("No")
    elif(difa[0] == difa[1] and difb[0] == difb[1] and diffS == 2):
        print("Yes")
    else:
        print("No")
