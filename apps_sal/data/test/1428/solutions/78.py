n, c = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(c)]
C = [list(map(int, input().split())) for _ in range(n)]

CC = [[0] * c for _ in range(3)]

for h, line in enumerate(C):
  for w, i in enumerate(line):
    CC[(h + w) % 3][i - 1] += 1
    
ans = 10 ** 19
for i in range(c):
  for j in range(c):
    for k in range(c):
      if i != j and j != k and k != i:
        score = 0
        score += sum(D[itr][i] * val for itr, val in enumerate(CC[0]))
        score += sum(D[itr][j] * val for itr, val in enumerate(CC[1]))
        score += sum(D[itr][k] * val for itr, val in enumerate(CC[2]))
        ans = min(ans, score)

print(ans)
