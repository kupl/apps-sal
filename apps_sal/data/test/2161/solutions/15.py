def same(x,y):
    if(len(x)>len(y)):
        if(y==x[len(x)-len(y):]):
            return 2
    else:
        if(x==y[len(y)-len(x):]):
            return 1
        else:
            return 0
    return 0

n=int(input())
pb=dict()
for i in range(n):
    record=input().split()
    if(record[0] in list(pb.keys())):
        pb[record[0]]+=record[2:]
    else:
        pb[record[0]]=record[2:]
for i in list(pb.keys()):
    rf=[]
    for j in pb[i]:
        flag=True
        for k in range(len(rf)):
            if(same(j,rf[k])==2):
                flag=False
                rf[k]=j
            elif(same(j,rf[k])==1):
                flag=False
        if(flag):
            rf.append(j)
    pb[i]=rf
print(len(list(pb.keys())))
for i in list(pb.keys()):
    print(i,len(pb[i]),*pb[i])
        

