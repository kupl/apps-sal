N=int(input())
Slide=dict()
SlideList=[list()]*N
ItogInformation=set()
GoodNameTags=set()

NewName,NewVer=input().split()
NewVer=int(NewVer)

GoodNameTags.add(NewName)

Slide[0]=NewName+' '+str(NewVer)
Slide[NewName+' '+str(NewVer)]=0
NewNum=int(input())
SlideList[0]=[0]*(NewNum+2)
SlideList[0][1]=NewNum

for i in range(1,NewNum+1):
    Name,Ver=input().split()
    SlideList[0][i+1]=Name+' '+Ver
    
for j in range(1,N):
    input()
    NewName,NewVer=input().split()
    NewVer=int(NewVer)
    Slide[j]=NewName+' '+str(NewVer)
    Slide[NewName+' '+str(NewVer)]=j
    NewNum=int(input())
    SlideList[j]=[0]*(NewNum+2)
    SlideList[j][1]=NewNum
    for i in range(1,NewNum+1):
        Name,Ver=input().split()
        SlideList[j][i+1]=Name+' '+Ver

ListOfNeed=set()
ListOfRead=set()
ListOfRead.add(Slide[0])

while len(ListOfRead)!=0:
    ListOfNeed=ListOfRead.copy()
    ListOfRead=set()
    found=dict()
    for i in ListOfNeed:
        for j in range(SlideList[Slide[i]][1]):
            Name,Ver=SlideList[Slide[i]][j+2].split()
            Ver=int(Ver)
            key=found.pop(Name, -1)
            if key==-1 or key<Ver:
                found[Name]=Ver
            else:
                found[Name]=key
    for i in list(found.keys()):
        if not (i in GoodNameTags):
            GoodNameTags.add(i)
            ListOfRead.add(i+' '+str(found[i]))
            ItogInformation.add(i+' '+str(found[i]))
    
Otvet=list(ItogInformation)
Otvet.sort()            

print(len(Otvet))
for i in range(len(Otvet)):
    print(Otvet[i])


