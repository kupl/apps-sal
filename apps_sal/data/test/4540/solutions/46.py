N = int(input())
A = list(map(int,input().split()))
A = [0] + A + [0]

cost = [0] * (N + 2)
for i in range(N+1):
  cost[i] += abs(A[i+1] - A[i])
  
sum_money = sum(cost)
  
skip = [0] * N
for j in range(N):
  skip[j] += abs(A[j+2] - A[j])
  
for k in range(N):
  print(sum_money - (cost[k] + cost[k+1]) + skip[k])
