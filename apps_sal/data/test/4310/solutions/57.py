A = list(map(int, input().split()))
line = [[0, 1, 2], [0, 2, 1], [1, 0, 2], 
        [1, 2, 0], [2, 0, 1], [2, 1, 0]]
ans = sum(A)

for i in range(len(line)):
  tmp = 0
  for j in range(1,3):
    tmp += abs(A[line[i][j]] - A[line[i][j-1]])
  ans = min(ans, tmp)
print(ans)

