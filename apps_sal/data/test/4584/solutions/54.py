n = int(input())
a =list(map(int,input().split()))
b = sorted(a)
c = [0]*n
for i in range(0,n-1):
  c[a[i]-1]+=1
for i in range(n):
  print(c[i])
