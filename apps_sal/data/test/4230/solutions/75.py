X, N=map(int, input().split())
if N==0:print(X);return
p=sorted(list(map(int, input().split())))

m=X;i=0
for i in range(m,min(p)-2,-1):
  if i not in p:break
M=X;j=0
for j in range(M,max(p)+2):
  if j not in p:break
if abs(i-X)==abs(j-X):print(min(i,j))
elif abs(i-X)<abs(j-X):
  print(i)
else:print(j)
