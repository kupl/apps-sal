N = int(input())
A = []
for _ in range(N):
  A.append(int(input()))
AA = sorted(A)
most = AA[N-1]
second = AA[N-2]

for i in range(N):
  if A[i] == most:
    print(second)
  else:
    print(most)
