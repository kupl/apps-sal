N = int(input())
A = list(map(int, input().split()))
AA = sorted(A)
X = AA[N//2 - 1]
Y = AA[N//2]
for i in range(N):
  if A[i] < Y:
    print(Y)
  if A[i] >= Y:
    print(X)
