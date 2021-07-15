import sys
input = sys.stdin.readline
n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
league = [0]*(n+1)
cnt = 0

while True:
  topop = []
  if cnt == 0:
    for i,player in enumerate(a):
      x = player[-1]
      if league[x] == i+1:
        topop.append(x)
        topop.append(i+1)
      else:
        league[i+1] = x
  else:
    for player in popped:
      if a[player-1] == []:
        continue
      x = a[player-1][-1]
      if league[x] == player:
        topop.append(x)
        topop.append(player)
      else:
        league[player] = x
  popped = []
  if topop == []:
    print((-1))
    return
  for t in topop:
    if a[t-1] == []:
      print((-1))
      return
    a[t-1].pop()
    popped.append(t)
  cnt += 1
  if not any(a[i] for i in range(n)):
    break
print(cnt)

