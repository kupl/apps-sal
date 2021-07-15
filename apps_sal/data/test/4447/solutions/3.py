k=int(input().split()[1])
l=list()
sc=[0]*k
for i in input().split():
    l.append(int(i))
goal=len(l)/k
cpt=0
s=""
dict={}
for i in range(len(l)):
    ok=0
    init=l[i]%k
    ltc=list()
    while(not ok):
        div=l[i]%k
        if(sc[div]<goal):
            sc[div]+=1
            ok=1
            for j in ltc:
                dict[j]=div
        else:
            ltc.append(div)
            #chercher dans la map si on a déjà été ici
            if(div in dict.keys()):
                nd=dict[div]
                diff=(nd-div)%k
                cpt+=diff
                l[i]+=diff
            else:
                cpt+=1
                l[i]+=1
    s+=str(l[i])+" "
print(cpt)
print(s[:len(s)-1])
