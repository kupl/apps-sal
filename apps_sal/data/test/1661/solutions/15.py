def ma():
  return list(map(int, input().split()))
n, m = ma()
i, j = 0, 0
A = list(ma())
B = list(ma())
ans = 0
while i < len(A) and j < len(B):
  if A[i] <= B[j]:
    j += 1
    i += 1
    ans += 1
  else:
    i += 1
print(ans)

