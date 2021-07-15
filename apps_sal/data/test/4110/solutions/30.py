from itertools import product

D, G = map(int, input().split())
G //= 100
prob = []

for i in range(1, D+1):
  p, c = map(int, input().split())
  prob.append((i, p, c//100))

ans = 1000
for comp in product((0, 1), repeat=D):
  cnt, score = 0, 0
  for i, c in enumerate(comp):
    if c:
      cnt += prob[i][1]
      score += prob[i][0]*prob[i][1] + prob[i][2]
  j = D-1
  while score < G and j >= 0:
    if comp[j] == 0:
      if score + prob[j][0]*prob[j][1] <= G:
        cnt += prob[j][1]
        score += prob[j][0]*prob[j][1]
      else:
        temp = -(-(G - score)//prob[j][0])
        cnt += temp
        score += prob[j][0]*temp
    j -= 1
  ans = min(ans, cnt)

print(ans)
