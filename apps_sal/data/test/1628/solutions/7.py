ins=input()
kol_x=0
kol_y=0
for ii in ins:
    if ii=='x': kol_x+=1
    else: kol_y+=1
if kol_x>kol_y:
    print('x'*(kol_x-kol_y))
else:
    print('y'*(kol_y-kol_x))

