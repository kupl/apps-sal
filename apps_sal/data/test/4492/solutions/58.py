N,X = map(int,input().split())
A = list(map(int,input().split()))
wa = []
ans = 0

if A[0] > X:
  ans += A[0]-X
  A[0] = X

for i in range(N-1):
  wa.append(A[i]+A[i+1])

for j in range(N-2):
  if wa[j] > X:
    ans += wa[j]-X
    wa[j+1] -= wa[j]-X

if wa[N-2] > X:
  ans += wa[N-2]-X

print(ans)
