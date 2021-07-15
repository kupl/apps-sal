menu=[]
menu2=[]
total=False
c=0
total2=0
for i in range(5):
    a=int(input())
    menu.append(a)
    menu2.append(a%10)
    if a%10==0:
        total2+=1
if total2==5:
    print(sum(menu))
else:
    for i in range(1,10):
        for k in range(5):
            if menu2[k]==i:
                total=True
                c=k
                break
        if total==True:
            break
    print(sum(menu)+10*(4-total2)-sum(menu2)+menu2[c])
