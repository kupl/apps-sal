import sys
readline = sys.stdin.readline

import heapq as hq

N,Q = list(map(int,readline().split()))
NN = 2 * (10 ** 5)

# (レート, 所属園)
infants = [None] * (N + 1)
# (最強園児, 園児番号)
kinda = [[] for i in range(NN + 1)]
for i in range(N):
  a,b = list(map(int,readline().split()))
  infants[i + 1] = [a,b]
  hq.heappush(kinda[b], (-a, i + 1))

# (最弱園児, 園の番号)
all_kinda = []
for i in range(len(kinda)):
  if kinda[i]:
    hq.heappush(all_kinda, (-kinda[i][0][0], i))
  
def get_max_rate(x): # 園xの最強レートを取り出す
  q = kinda[x]
  while q:
    rate, ind = hq.heappop(q)
    if infants[ind][1] != x:
      continue
    hq.heappush(q, (rate, ind))
    return -rate
  return -1
  
for i in range(Q):
  ind,next_kinda_id = list(map(int,readline().split()))
  rate,old_kinda_id = infants[ind]
  infants[ind][1] = next_kinda_id
  hq.heappush(kinda[next_kinda_id],(-rate, ind))
  
  old_kinda_max_rate = get_max_rate(old_kinda_id)
  if old_kinda_max_rate != -1:
    hq.heappush(all_kinda, (old_kinda_max_rate, old_kinda_id))
    
  next_kinda_max_rate = get_max_rate(next_kinda_id)
  if next_kinda_max_rate != -1:
    hq.heappush(all_kinda, (next_kinda_max_rate, next_kinda_id))
    
  while all_kinda:
    rate, kinda_id = hq.heappop(all_kinda)
    cur_max_rate = get_max_rate(kinda_id)
    if rate != cur_max_rate:
      continue
    hq.heappush(all_kinda, (rate, kinda_id))
    print(rate)
    break

