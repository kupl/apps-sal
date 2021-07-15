import copy
n, T = list(map(int, input().split()))
A = list(map(int, input().split()))
s = sum(A)
ans = 0
B = []
for a in A:
  if a <= T:
    B.append(a)
  else:
    s -= a
while len(B) > 0:
  loop = T // s
  if loop == 0:
    for i in range(len(A)):
      if T >= A[i]:
        ans += 1
        T -= A[i]    
  else:
    ans += loop * len(B)
    T %= s
    
  A = copy.deepcopy(B)
  B = []
  for a in A:
    if a <= T:
      B.append(a)
    else:
      s -= a
print(ans)
