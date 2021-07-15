S=input()
pr=10**9+7
a1,a2,a3=0,0,0
c=0
for i in S:
    if i=="A":
        a1=(a1+pow(3,c,pr))%pr
    elif i=="B":
        a2=(a2+a1)%pr
    elif i=="C":
        a3=(a3+a2)%pr
    else:
        a1,a2,a3=(3*a1+pow(3,c,pr))%pr,(3*a2+a1)%pr,(3*a3+a2)%pr
        c+=1
print(a3)
