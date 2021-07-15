N,X,Y = map(int,input().split())
a = [0]*(N-1)
for i in range(1,N):
  for j in range(i+1,N+1):
    ans = min(j-i,abs(X-i)+1+abs(Y-j),abs(X-j)+1+abs(Y-i))
    a[ans -1] += 1
for item in a:
  print(item)
