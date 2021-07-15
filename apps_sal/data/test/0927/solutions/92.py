N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A.reverse()

match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [-N-N] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
  for j in A:
    if i >= match[j]:
      dp[i] = max(dp[i], dp[i - match[j]] + 1)

max_list = []
while N:
  for j in A:
    if N >= match[j] and dp[N] == dp[N - match[j]] + 1:
      max_list.append(j)
      N -= match[j]
      break

for j in max_list:
  print(j, end="")
print("")
