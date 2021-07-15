N, K = map(int, input().split())

d = [0 for i in range(K)]
A = []
for i in range(K):
  d[i] = int(input())
  A.append(list(map(int, input().split())))

candy = [0 for i in range(N)]
for i in range(K):
  for j in range(d[i]):
    candy[A[i][j]-1] += 1
print(candy.count(0))
