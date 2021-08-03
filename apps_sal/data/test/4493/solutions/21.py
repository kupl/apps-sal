clst = list(map(int, input().split()))
dif = [x - clst[0] for x in clst]
clst = list(map(int, input().split()))
if not [clst[0] + x for x in dif] == clst:
    print("No")
    return
clst = list(map(int, input().split()))
if not [clst[0] + x for x in dif] == clst:
    print("No")
    return
print("Yes")
