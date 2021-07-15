N, D, A = list(map(int, input().split()))
monster = []
for k in range(N):
  monster.append(list(map(int, input().split())))
monster.sort(key = lambda x: x[0])
for k in range(N):
  monster[k][1] = int((monster[k][1]-0.1)//A + 1)
ans = 0

final = monster[-1][0]
ruiseki = 0
minuslist = []
j = 0
for k in range(N):
  while (j < len(minuslist)):
    if monster[k][0] >= minuslist[j][0]:
      ruiseki -= minuslist[j][1]
      j += 1
    else:
      break
  if ruiseki < monster[k][1]:
    ans += monster[k][1] - ruiseki
    if monster[k][0] + 2*D +1 <= final:
      minuslist.append([monster[k][0]+2*D+1, monster[k][1] - ruiseki])
    ruiseki = monster[k][1]


print(ans)

