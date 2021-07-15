N, C = map(int, input().split())
XV = []

for _ in range(N):
  x, v = map(int, input().split())
  XV.append((x, v))

#R:右回りでそこまで行くときの満足度
#Rr:右行って引き返す時の最大満足度
R = [0]
Rr = [0]
for x, v in XV:
  R.append(R[-1] + v)
  Rr.append(Rr[-1] + v)
for i, (x, v) in enumerate(XV):
  R[i+1] -= x
  Rr[i+1] -= 2*x
for i in range(N):
  Rr[i+1] = max(Rr[i+1], Rr[i])

#左バージョン
L = [0]
Lr = [0]
for x, v in reversed(XV):
  L.append(L[-1] + v)
  Lr.append(Lr[-1] + v)
for i, (x, v) in enumerate(reversed(XV)):
  L[i+1] -= (C-x)
  Lr[i+1] -= 2*(C-x)
for i in range(N):
  Lr[i+1] = max(Lr[i+1], Lr[i])

#print(R, Rr, L, Lr)
ans = 0

for i in range(1, N+1):
  temp = max(R[i], R[i] + Lr[N-i], L[N+1-i], L[N+1-i] + Rr[i-1])
  ans = max(ans, temp)

print(ans)
