k=int(input())
n=50
a=[n-1]*n
m=k%n
for i in range(n):
  a[i]+=k//n
  if i<m:a[i]+=n-m+1
  else:a[i]+=-m
print(n)
print(*a)
