N, X, Y = map(int, input().split())
A = [N - i for i in range(1, N)]
for i in range(N-1):
  for j in range(i+1, N):
    c = min(abs(X-i-1)+abs(Y-j-1)+1, abs(X-j-1)+abs(Y-i-1)+1)
    if c < j-i:
      A[j-i-1] -= 1
      A[c-1] += 1
for a in A:
  print(a)
