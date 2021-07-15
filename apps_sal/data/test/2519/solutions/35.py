N, K = map(int, input().split())
p = list(map(int, input().split()))
  
# 「和の期待値」は「期待値の和」なので、先に期待値を求める
for i in range(N):
  p[i] = (1+p[i])/2

# 累積和
S = [0]*N
S[0] = p[0]
for i in range(N-1):
  S[i+1] = S[i] + p[i+1]

ans = S[K-1]
for i in range(N-K):
  ans = max(ans, S[i+K] - S[i])

print(ans)
