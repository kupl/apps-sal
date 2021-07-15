n=int(input())
p=list(map(int,input().split()))
x=list(map(int,input().split()))
y=[0]*n
c=[[]for _ in[0]*n]
for i in range(n-1):c[p[i]-1]+=[i+1]
I=float('inf')
for i in range(n-1,-1,-1):
 a=x[i];d=[0]*-~a
 for j in c[i]:
  for k in range(a,-1,-1):b=x[j];e=y[j];f=I if k-b<0else d[k-b]+e;g=I if k-e<0else d[k-e]+b;d[k]=min(f,g,I)
 y[i]=d[a]
print('POSSIBLE'if I>y[0]else'IMPOSSIBLE')
