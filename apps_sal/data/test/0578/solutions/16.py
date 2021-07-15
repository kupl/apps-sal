

calcul=input()
n=len(calcul)
e=None
for i in range(n):
        if calcul[i]=="e":
                e=i
a=calcul[0]
d=calcul[2:e]
b=int(calcul[e+1:])

if d=="0":
        d=""

if len(d)==b:
        resultat=a+d
elif b>len(d):
        nombreZero=b-len(d)
        resultat=a+d+"0"*nombreZero
else:
        add=a+d
        virgule=b-len(d)
        resultat=add[:virgule]+"."+add[virgule:]

        inf=0
        sup=len(resultat)-1
        while resultat[inf]=="0" and sup>inf:
                inf+=1
        while resultat[sup]=="0" and sup>inf:
                sup-=1
        if resultat[inf]==".":
                resultat="0"+resultat[inf:sup+1]
        else:
                resultat=resultat[inf:sup+1]
        
print(resultat)





        

