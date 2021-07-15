P = 10**9+7
nn = 2000
fa = [1] * (nn+1)
fainv = [1] * (nn+1)
for i in range(nn):
    fa[i+1] = fa[i] * (i+1) % P
fainv[-1] = pow(fa[-1], P-2, P)
for i in range(nn)[::-1]:
    fainv[i] = fainv[i+1] * (i+1) % P
 
C = lambda a, b: fa[a] * fainv[b] % P * fainv[a-b] % P if 0 <= b <= a else 0

N = int(input())
if N < 4:
  print(1)
  return
c = []
for _ in range(4):
  c.append(input())
if c[1] == "A":
  if c[0] == "A":
    print(1)
  else:
    if c[2] == "B":
      N -= 3
      ans = 1
      for _ in range(N):
        ans = 2*ans%P
      print(ans)
    else:
      N -= 3
      M = N//2
      ans = 0
      for m in range(M+1):
        a = N-m
        ans = (ans + C(a,m))%P
        ans = (ans + C(a,m-1))%P
      if N%2==1:
        ans = (ans+1)%P
      print(ans)
else:
  if c[3] == "B":
    print(1)
  else:
    if c[2] == "A":
      N -= 3
      ans = 1
      for _ in range(N):
        ans = 2*ans%P
      print(ans)
    else:
      N -= 3
      M = N//2
      ans = 0
      for m in range(M+1):
        a = N-m
        ans = (ans + C(a,m))%P
        ans = (ans + C(a,m-1))%P
      if N%2==1:
        ans = (ans+1)%P
      print(ans)
