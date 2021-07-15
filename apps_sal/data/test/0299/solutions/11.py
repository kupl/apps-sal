sa=input()
sa2=input().split(' ')
sa3=[int(x) for x in sa2]
chest=0
biceps=0
back=0
for x in range(len(sa3)):
    if (x+1)%3==1:
        chest+=sa3[x]
    elif (x+1)%3==2:
        biceps+=sa3[x]
    else:
        back+=sa3[x]

if max(chest, back, biceps)==chest:
    print("chest")
if max(chest, back, biceps)==back:
    print("back")
if max(chest, back, biceps)==biceps:
    print("biceps")

