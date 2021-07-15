n,d=list(map(int,input().split()))
sk = list(map(int,input().split()))
pk=list(map(int,input().split()))

sk[d-1] += pk[0]
pk.pop(0)
rank=1

for i in range(d-1):
    if sk[i]+pk[-1]>sk[d-1]:
        rank+=1
    elif sk[i]+pk[-1]==sk[d-1]:
        pk.pop()
        
    else:
        j=len(pk)-1
        pk.pop(j)            
    

print(rank)

    

