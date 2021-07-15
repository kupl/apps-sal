N,A,B = map(int,input().split())
V = sorted(list(map(int,input().split())))[::-1]
W = sum(V[:A])/A
print(W)

f = [1]
for n in range(50):
  f+=[f[-1]*(n+1)]
x = V.count(V[A-1])
if V[0]==V[A-1]:
  print(sum(f[x]//(f[x-n]*f[n]) for n in range(A,B+1)))
else:
  y=V[:A].count(V[A-1])
  print(f[x]//(f[x-y]*f[y]))
