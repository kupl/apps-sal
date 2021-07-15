maxa=(10)**11
N=int(input())
L=list(map(int,input().split()))
for i in range(-100,101):
  R=[(i-y)**2 for y in L]
  a=sum(R)
  maxa=min(maxa,a)
print(maxa)
