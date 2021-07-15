n=int(input().strip())
numbers=tuple(map(int,input().strip().split()))
occ=[0 for i in range(100001)]
places=[]
d={}
for k in range(0,len(numbers)):
    occ[numbers[k]]+=1
    if(occ[numbers[k]]-1 in list(d.keys())):
        if(d[occ[numbers[k]]-1]==1):
            d.pop(occ[numbers[k]]-1 )
        else:
            d[occ[numbers[k]]-1]-=1
    if(occ[numbers[k]] in list(d.keys())):
        d[occ[numbers[k]]]+=1
    else:
        d[occ[numbers[k]]]=1
    if(len(list(d.keys()))==2 and (1 in list(d.keys())) and (2 in list(d.keys()))):
        if(d[2]==1):
            places.append(k)
        if(d[1]==1):
            places.append(k)
    elif(len(list(d.keys()))==2 and (1 in list(d.keys()))):
        if(d[1]==1):
            places.append(k)
    elif(len(list(d.keys()))==2 ):
        lll=list(d.keys())
        if(lll[0]-lll[1]==1):
            if(d[lll[0]]==1):
                places.append(k)
        if (lll[1] - lll[0] == 1):
            if (d[lll[1]] == 1):
                places.append(k)
    elif(len(list(d.keys()))==1):
        jo=1
        for i in list(d.keys()):
            if(d[i]==1):
                places.append(k)
                jo=0
        if(jo):
            if(1 in list(d.keys())):
                places.append(k)
if(len(places)>0):
    print(places[-1]+1)
else:
    print(0)





