N, A,B,*V = map(int,open(0).read().split())
V = sorted(V)[::-1]
ans1 = sum(V[:A])/A
print(ans1)
f = [1] *51
for i in range(1,51):
  f[i] = f[i - 1] * i
def comb(n,r):
  return f[n]//f[r]//f[n-r]
ans2 = comb(V.count(V[A-1]),V[:A].count(V[A-1]))
if V[0] == V[A-1]:
  for i in range(A+1,B+1):
    ans2 += comb(V.count(V[A-1]),i)
print(ans2)
