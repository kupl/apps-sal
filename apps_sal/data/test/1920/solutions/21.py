
arrMa=[0]*367
arrFe=[0]*367
p=int(input())

for i in range(p):
    inf=list(map(str,input().split()))
    if inf[0]=='M':
        arrMa[int(inf[1])-1]+=1
        arrMa[int(inf[2])]-=1
    else:
        arrFe[int(inf[1])-1]+=1
        arrFe[int(inf[2])]-=1
        
maxi=-1
curM=0
curF=0
for i in range(366):
    curM+=arrMa[i]
    curF+=arrFe[i]
    if min(curM,curF)>maxi:
        maxi=min(curM,curF)
    
print(maxi*2)

