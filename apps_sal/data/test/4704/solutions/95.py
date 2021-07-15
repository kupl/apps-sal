N=int(input())
L=list(map(int,input().split()))
sums=0
a=sum(L)
mina=10**10
for i in range(N-1):
  a-=2*L[i]
  mina=min(mina,abs(a))
print(mina)
