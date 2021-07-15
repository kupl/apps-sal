n,k,q = map(int,input().split())
l = [k-q]*n
for i in range(q):
  a = int(input())
  l[a-1]+=1
for j in range(n):
  if l[j]<=0:
    print("No")
  else:
    print("Yes")
