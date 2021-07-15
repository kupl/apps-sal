k=int(input())
n=50
a=[49]*n
x=k//n
y=k%n
for i in range(n):
  a[i]+=x
  if i<y:a[i]+=(n+1)-y
  else:a[i]-=y
print(n)
print(*a)
