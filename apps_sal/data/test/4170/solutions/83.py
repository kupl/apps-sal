N = int(input())
L = list(map(int,input().split()))
M = [0] * N
for i in range(1 , N):
  if L[i] <= L[i - 1]:
    M[i] = M[i - 1] + 1
print((max(M)))


