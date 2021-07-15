n=int(input())
raby=[x for x in input()]
numD=0
numR=0
flag=True
while flag: 
    cR=0
    cD=0
    for ind in range(len(raby)):
        if raby[ind]=='D':
            cD+=1
            if numR==0:
                numD+=1
            else:
                raby[ind]='N'
                numR-=1
        if raby[ind]=='R':
            cR+=1
            if numD==0:
                numR+=1
            else:
                raby[ind]='N'
                numD-=1
    if cD==0 or cR==0:
            flag=False
if numD==0:
    print('R')
else:
    print('D')
