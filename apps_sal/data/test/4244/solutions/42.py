N=int(input())
X=sorted(list(map(int,input().split())))
Y=[0]*(max(X)-min(X)+1)
s=0
for i in range(max(X)-min(X)+1):
  for j in X:
    Y[i]+=(j-i-min(X))**2

print(min(Y))
