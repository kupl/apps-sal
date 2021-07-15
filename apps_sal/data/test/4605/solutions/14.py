N,A,B=map(int,input().split())
X=[]
for i in range(1,N+1):
  if A<= sum(list(map(int,str(i)))) <=B:
    X.append(i)
print(sum(X))
