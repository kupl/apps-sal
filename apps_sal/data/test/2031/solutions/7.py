n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  a[i]=[a[i],n-i]
a.sort()
c=list(range(n))
for i in range(n):
  c[n-i-1]=[n-a[i][1]+1,a[i][0]]
m=int(input())
for g in range(m):
  k,pos=list(map(int,input().split()))
  b=c[:k]
  b.sort()
  print(b[pos-1][1])

