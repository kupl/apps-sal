N,K = map(int, input().split())
S = input()

A = []
pre = S[0]
cnt = 1
for i in range(1,N):
  if pre == S[i]:
    cnt += 1
  else:
    pre = S[i]
    A.append(cnt)
    cnt = 1
A.append(cnt)
if len(A) == 1:
  print(N-1)
  return
ans = sum(A) - len(A)
# X は真ん中。Yは端っこ。引数はIndexのMOD2。
X,Y = [0,0], [0,0]
for i in range(len(A)):
  if i == 0 or i == len(A)-1:
    Y[i%2] += 1
  else:
    X[i%2] += 1
    
wk = [0,0]
for i in range(2):
  if K <=X[i]:
    wk[i] = K * 2
  elif K <= X[i] + Y[i]:
    wk[i] = X[i] * 2 + (K-X[i])
  else:
    wk[i] = X[i] * 2 + Y[i]

print(ans + max(wk))
return
print(ans, wk)
print(A)
print(X)
print(Y)
