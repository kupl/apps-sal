a=int(input())
b=list(map(int,input().split()))
d=0
for i in range(a):
  d=d+(1/b[i])
print(1/d)
