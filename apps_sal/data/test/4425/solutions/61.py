import math
N, K = map(int, input().split())
 
ans = 0

# 目がK-1以下 => コインが ceil(log2(K/i)) 回連続で表で勝ち
# 目がK以上 => 勝ち確定
for i in range(1, N+1):
  if i <= K-1: ans += (1/N)*(1/2)**math.ceil(math.log2(K/i))
  else: ans += 1/N
print(ans)
