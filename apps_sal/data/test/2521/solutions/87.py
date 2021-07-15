import heapq

n=int(input())
a1=[]
b1=[]
a2=[]
b2=[]
s=input().split()
for i in range(3*n):
    if i<n:
        a1.append(int(s[i]))
    elif i>=2*n:
        b1.append(-int(s[i]))
    else:
        a2.append(int(s[i]))
        b2.append(-int(s[3*n-i-1]))
suma=[sum(a1)]
sumb=[sum(b1)]
heapq.heapify(a1)
heapq.heapify(b1)

for i in range(0,n):
    heapq.heappush(a1,a2[i])
    k=heapq.heappop(a1)
    l=suma[-1]
    suma.append(l+a2[i]-k)
for i in range(0,n):
    heapq.heappush(b1,b2[i])
    k=heapq.heappop(b1)
    l=sumb[-1]
    sumb.append(l+b2[i]-k)

ma=-1000000000000000
for i in range(n+1):
    ma=max(ma,suma[i]+sumb[-i-1])
print(ma)

