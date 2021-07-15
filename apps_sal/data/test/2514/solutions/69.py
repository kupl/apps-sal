n=int(input())
l=[0]*(10**5+1)
k=list(map(int,input().split()))
q=int(input())
for i in range(n):
    l[k[i]]+=1
wa=sum(k)
for i in range(q):
    a,b=map(int,input().split())
    wa+=(b-a)*l[a]
    print(wa)
    l[b]+=l[a]
    l[a]=0
