N,K=map(int,input().split())
A=list(map(int,input().split()))

dic={}
for i in range(N+1):
    dic[i]=0
for i in A:
    dic[i]+=1

dic_sort=sorted(dic.values(),reverse=True)

print(sum(dic_sort[K:]))
