from collections import Counter

n, k = list(map(int, input().split()))
h = list(map(int, input().split()))

cnt = Counter(h)

elems = 0
costs = []

hs = list(reversed(sorted(cnt.keys())))
cur_sum = 0
ans = 0

for i in range(len(hs) - 1):
  v, c = hs[i], cnt[hs[i]]
  next_v = hs[i+1]
  diff = v - next_v
  elems += c

  if cur_sum + elems > k:
    ans += 1
    cur_sum = 0
  
  if cur_sum + diff * elems <= k:
    cur_sum += diff * elems
  else:
    if cur_sum != 0:
      diff -= (k - cur_sum) // elems
      ans += 1
    per_cut = k // elems
    cuts = diff // per_cut
    cur_sum = (diff % per_cut) * elems
    ans += cuts
    
ans += cur_sum > 0
print(ans)
