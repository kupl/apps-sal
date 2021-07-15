from collections import defaultdict
pr = defaultdict(int)
N = 2750132 
d = [0]*N
k = 1
for i in range(2,N):
    if d[i]==0:
        d[i] = 1
        pr[i] = k
        k+=1
        for j in range(i*i,N,i):
            if d[j]==0:
                d[j] = max(i,j//i)

c = [0]*(N)
n = int(input())
a = list(map(int,input().split()))
for i in a:
    c[i]+=1
    
ans = []


for i in range(N-1,2,-1):
    if c[i]>0:
        if pr[i]==0:
            t = d[i]
            for j in range(c[i]):
                ans.append(i)
            c[t]-=c[i]
        else:
            k = pr[i]
            for j in range(c[i]):
                ans.append(k)
            c[k]-=c[i]

print(*ans)

