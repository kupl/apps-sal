occount = input()
oc = [int(i) for i in input().split()]
podar = 0
while len(oc) >= 3:
    if (oc[0] == 5 or oc[0] == 4) and (oc[1] == 5 or oc[1] == 4) and (oc[2] == 5 or oc[2] == 4):
        podar = podar + 1
        del oc[0]
        del oc[0]
        del oc[0]
    else:
        del oc[0]
print(podar)
