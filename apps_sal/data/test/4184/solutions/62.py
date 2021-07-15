N=int(input())
W=[int(_) for _ in input().split()]
r=max(W)
for i in range(1,N):
  if (_:=abs(sum(W[:i])-sum(W[i:]))) < r: r=_
print(r)
