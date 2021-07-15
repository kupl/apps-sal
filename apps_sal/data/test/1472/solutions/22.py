N, X, Y = map(int, input().split())
L = [0]*(N+1)

for i in range(1, N):
  for j in range(i+1, N+1):
    L[(min(j-i, abs(X-i)+1+abs(Y-j)))] += 1
for i in range(1, N):
  print(L[i])
