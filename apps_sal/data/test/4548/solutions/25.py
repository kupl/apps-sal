N, M, X = [int(i) for i in input().split()]
AS = [int(i) for i in input().split()]

cnt1 = 0
for i in range(0, X):
  if i in AS:
    cnt1 += 1

cnt2 = 0
for i in range(X+1, N+1):
  if i in AS:
    cnt2 += 1

print((cnt1 if cnt1 < cnt2 else cnt2))

