from itertools import accumulate
from collections import Counter
N,K,*A = map(int, open(0).read().split())
A = [a-1 for a in A]
B = [b%K for b in accumulate(A)]
if K>N:
  Cnt = Counter(B)
  ans = Cnt[0]+sum(v*(v-1)//2 for v in Cnt.values())
else:
  Cnt = Counter(B[:K])
  ans = Cnt[0]+sum(v*(v-1)//2 for v in Cnt.values())
  if B[K-1]==0:
    ans -= 1
  for i in range(N-K):
    Cnt[B[i]] -= 1
    ans += Cnt[B[i+K]]
    Cnt[B[i+K]] += 1
print(ans)
