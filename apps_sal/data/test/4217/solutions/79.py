n,m = map(int,input().split())
ans = set(range(1,31))
for i in range(n):
  kA = list(map(int,input().split()))
  k = kA[0]
  A = kA[1:]
  ans = ans & set(A)
print(len(ans))
