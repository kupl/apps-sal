n = int(input())
a =list(map(int,input().split()))
d = [0]*(n+1)
answer = 0
for i in range(n):
  d[a[i]]+=1
for j in range(n+1):
  answer+= (d[j]*(d[j]-1))//2
for k in range(n):
  print(answer+1-(d[a[k]]))
