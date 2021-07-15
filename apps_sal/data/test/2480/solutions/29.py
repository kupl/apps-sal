from collections import Counter
N,K = map(int, input().split())
A = list(map(int, input().split()))
A = list(map(lambda x: x%K, A))

"""
j - i < K and
Sj - Si == j - i (mod K)
Sj - j == Si - i (mod K) この変形が肝だ…
"""

S = [0 for _ in range(N+1)]
for i in range(N):
  S[i+1] = (S[i] + A[i] - 1) % K
ans = 0
C = Counter(S[:K])
for k,v in C.items():
  ans += v * (v-1) // 2
  
for i in range(K,N+1):
  deln = S[i-K]
  C[deln] -= 1
  addn = S[i]
  if addn in C:
    ans += C[addn]
    C[addn] += 1
  else:
    C[addn] = 1
    
print(ans)
