a=int(input())
b=int(input())
c=list(map(int,input().split()))
d=0
for i in range(a):
  if c[i]<b-c[i]:
    d=d+c[i]
  else:
    d=d+b-c[i]
print(2*d)
