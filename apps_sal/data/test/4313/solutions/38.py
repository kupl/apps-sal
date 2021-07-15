N=int(input())
V=list(map(int,input().split()))
C=list(map(int,input().split()))
l=[]
for i in range(N):
   if V[i]-C[i]>0:
       l.append(V[i]-C[i])
print(sum(l))
