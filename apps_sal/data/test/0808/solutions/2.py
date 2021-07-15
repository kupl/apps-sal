from sys import stdin,stdout


mot=stdin.readline()
virgule=None
for i in range(len(mot)):
        if mot[i]==".":
                virgule=i
if virgule!=None:
        mot=mot.replace(".","")
inf=0
sup=len(mot)-2

while mot[inf]=="0" and sup>inf:
        inf+=1
        
if virgule==None:
        puissance=sup-inf
else:
        puissance=virgule-inf-1

while mot[sup]=="0" and sup>inf:
        sup-=1

                
notation=mot[inf]

if inf==sup:
        notation=mot[inf]
else:
        notation=mot[inf]+"."+mot[inf+1:sup+1]

if puissance!=0:
        notation+="E"+str(puissance)
           
stdout.write(notation)




