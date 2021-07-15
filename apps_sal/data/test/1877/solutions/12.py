import math
n = int(input())
ans = 0
nr = 0
nu = 0
side = 0


mm = list(input())
fm = mm[0]
mm = mm[1:]

if fm == "U":
    side = 1
    nu = 1
else:
    side = -1
    nr = 1



for m in  mm:
    if nu==nr:

        if m =="U" and side == -1:
            ans +=1
            side = 1
        elif m == "R" and side == 1:
            ans += 1
            side = -1

    if m == "U":
        nu += 1
    else:
        nr +=1


print(ans)


