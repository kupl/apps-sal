N = int(input())
A = [None] * N

for i in range(N):
  A[i] = list(map(lambda x:int(x) - 1,input().split()))[::-1]
  
# A[i]の最後尾が、次に対戦する相手

# 次に試合する候補の人を全員洗い出す。最初は全員
playable = set(range(N))

day = 0
while True:
  next_playable = set() # 次の日に試合できる状態になる人
  done = set() # その日に既に試合を終えた人を管理
  for player in playable:
    if player in done:
      continue
    if len(A[player]) == 0:
      continue
    rival = A[player][-1]
    if rival in done:
      continue
    if len(A[rival]) == 0:
      continue
    if A[rival][-1] == player:
      done.add(player)
      done.add(rival)
      A[player].pop()
      A[rival].pop()
      # この二人は次の試合の探索対象となる
      next_playable.add(player)
      next_playable.add(rival)
  if len(next_playable) == 0:
    break
  playable = next_playable
  day += 1

# できる試合がなくなった状態で、全員の試合が終わっていればOK
ok = True
for i in range(len(A)):
  if len(A[i]) != 0:
    ok = False
    break
    
print((-1,day)[ok])
