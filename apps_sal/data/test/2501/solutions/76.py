N = int(input())
A = list(map(int, input().split()))
L = {}
R = {}
ans = 0
for i in range(N):
  t = i + 1 + A[i]
  if t in L:
    L[t] += 1
  else:
    L[t] = 1
  t = i + 1 - A[i]
  if t > 0:
    if t in R:
      R[t] += 1
    else:
      R[t] = 1
for i in R:
  if i in L:
    ans += R[i] * L[i]
print(ans)
