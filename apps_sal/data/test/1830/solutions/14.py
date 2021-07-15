A = input().split()
n=int(A[0])
m=int(A[1])
s=n**2
B = [0] * (n+1)
C = [0] * (n+1)
x1=n
y1=n
for i in range(m):
   A = input().split()
   x=int(A[0])
   y=int(A[1])
   if B[x]==0 and C[y]==0:
       s=s-x1-y1+1
       x1-=1
       y1-=1
   if B[x]==1 and C[y]==0:
       s=s-y1
       x1-=1
   if B[x]==0 and C[y]==1:
       s=s-x1
       y1-=1    
   B[x]=1
   C[y]=1
   print(s, end=' ')
   

