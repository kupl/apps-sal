n,x,y = map(int, input().split())
g = [0]*(n)
for i in range(1,n+1):
  for j in range(1,i):
    e = abs(y-i)+1+abs(x-j)
    f = i-j
    g[min(e,f)]+=1
for i in g[1:]:
  print(i)
