n,k=map(int,input().split());p=[]
while n:
  p.append(n%k)
  n//=k
print(len(p))
