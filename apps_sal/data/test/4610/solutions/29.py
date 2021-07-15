n,k=list(map(int, input().split()))
a_list=[int(i) for i in input().split()]

dic={}

for i in a_list:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

dic2=sorted(list(dic.items()), key=lambda x:x[1])

ans=0

if len(dic)>k:
    num=len(dic)-k
    for i in range(num):
        ans+=dic2[i][1]

    
print(ans)

