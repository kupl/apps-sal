def sumArr(ax):
    sm=0
    for i in range(len(ax)):
        sm+=(10**i)*ax[i]
    return sm

n=int(input())
arr={}
la='abcdefghij'
for i in la:
    arr.update({i:{'m':[0,0,0,0,0,0],'not0':False,'sm':0}})
while (n>0):
    n-=1
    x=input()[::-1]
    L=len(x)
    for i in range(L):
        arr[x[i]]['m'][i]+=1
        if i==L-1:
            arr[x[i]]['not0']=True
arrF=[]
arrT=[]
for i in la:
    arr[i]['sm']=sumArr(arr[i]['m'])
    if arr[i]['not0']:
        arrT.append(arr[i]['sm'])
    else:
        arrF.append(arr[i]['sm'])

arrF=sorted(arrF)
arrT=sorted(arrT)
arrF=arrF[::-1]
arrT=arrT[::-1]

iaT=0
if len(arrF)>0:
  iaF=1
  arrQ=[arrF[0]]
else:
  iaF=0
  arrQ=[0]
for i in range(9):
    mF,mT=-1,-1
    if iaT<len(arrT):
        mT=arrT[iaT]
    if iaF<len(arrF):
        mF=arrF[iaF]
    if mF>=mT:
        arrQ.append(mF)
        iaF+=1
    else:
        arrQ.append(mT)
        iaT+=1
sm=0

for i in range(len(arrQ)):
    sm+=arrQ[i]*i
print(sm)


