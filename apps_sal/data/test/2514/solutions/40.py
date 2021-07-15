N = int(input())
A = list(map(int,input().split()))
Q = int(input())
BC = list(list(map(int,input().split())) for _ in range(Q))

total = sum(A)

li = [0] * 100000
for i in range(N):
  li[A[i] - 1] += 1

for i in range(Q):
  j = BC[i][0]
  k = BC[i][1]
  if li[j - 1] > 0:
    li[k - 1] += li[j - 1]
    total += li[j - 1] * (k - j)
    li[j - 1] = 0
  print(total)
