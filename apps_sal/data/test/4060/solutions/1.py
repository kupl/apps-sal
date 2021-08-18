n = int(input())
l = list(input())
cptMoins = 0
cptPlus = 0
cpt = 0
dead = False
plusEnd = False
for k in range(n):
    if(l[k] == '('):
        cpt += 1
        cptMoins += 1
    else:
        cpt -= 1
        if(not plusEnd):
            cptPlus += 1
    if(cpt < -2):
        dead = True
        break
    if (cpt < 0):
        if(plusEnd or cptPlus == 0):
            dead = True
            break
        else:
            plusEnd = True
            cpt += 2

    if cpt < 2:
        cptMoins = 0
if(dead):
    print(0)
else:
    if(plusEnd and cpt == 0):
        print(cptPlus)
    elif (not plusEnd and cpt == 2):
        print(cptMoins)
    else:
        print(0)
