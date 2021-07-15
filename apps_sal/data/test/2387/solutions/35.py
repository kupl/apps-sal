from operator import itemgetter
N = int(input())

def checkNonnegative(brankets):
    curup = 0
    for (minup , up) in sorted(brankets , key= itemgetter(0) , reverse = True):
        if curup + minup < 0:
            return False
        curup += up
    return True

def canArrangeBranket(brankets):
    totup = 0
    left_brankets = []
    right_brankets = []
    for branket in brankets:
        up = 0
        minup = 0
        for c in list(branket):
            if c == '(':
                up += 1
            else:
                up -= 1
                minup = min(minup , up)
        totup += up
        if up >= 0:
            left_brankets.append((minup , up))
        else:
            right_brankets.append((minup - up , - up))
    if totup != 0:
        return False
    return checkNonnegative(left_brankets) and checkNonnegative(right_brankets)

branketList = []
for i in range(N):
    l = input()
    branketList.append(l)

if canArrangeBranket(branketList):
    print("Yes")
else:
    print("No")

