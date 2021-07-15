from collections import defaultdict
N,m=list(map(int,input().split()))
graph=defaultdict(list)
edges=[]
passages=[[] for i in range(N-1)]
for _ in range(m):
    u,v=list(map(int,input().split()))
    passages[u-1].append(v-1)
prob=[0]*N
prob[0]=1
for n,dest in enumerate(passages):
    #print(n,dest,'ndest')
    for d in dest:
        prob[d]+=prob[n]/len(dest)
# no blocking
e=[0]*N
#print(prob)
for n,dest in list(enumerate(passages))[::-1]:
    #print(dest,n,'n dess t')
    e[n]=sum(e[d] for d in dest)/len(dest)+1
min_e=e[0]
#with blocking
for n,dest in enumerate(passages):
    if len(dest)==1:
        continue
    new_e=((e[n]-1)*len(dest)-max(e[d] for d in dest))/(len(dest)-1)+1
    min_e=min(min_e,e[0]-(e[n]-new_e)*prob[n])
print(min_e)
    

        


