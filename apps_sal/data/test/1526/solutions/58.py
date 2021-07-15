A = list(map(int,input().split()))
A.sort()
ans = 0
while A[0] != A[1] or A[1] != A[2]:
  ans += 1
  if A[2] - A[0] > 1:
    A[0] += 2
  else:
    A[0] += 1
    A[1] += 1
  A.sort()
print(ans)
