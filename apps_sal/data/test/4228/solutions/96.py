n,l=map(int,input().split())
list_x=[l+x-1 for x in range(1,n+1)]
applepai=sum(list_x)
list_dif=[]
list_sum=[]
for i in range(len(list_x)):
    tmp=list_x.pop(i)
    list_dif.append(abs(applepai-sum(list_x)))
    list_sum.append(sum(list_x))
    list_x.insert(i,tmp)
indx=list_dif.index(min(list_dif))
ans=list_sum[indx]
print(ans)
