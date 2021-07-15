from collections import Counter

N, M = list(map(int, input().split()))
A = [int(i)%M for i in input().split()]

B = [0] * (N+1)
for i in range(N):
  B[i+1] = (B[i]+A[i]) % M
  
counter = dict(Counter(B))
ans = 0
for num in counter:
  ans += (counter[num]-1) * counter[num] // 2

print(ans)


