N,M = map(int,input().split())
key = []
for i in range(M):
  a,b = map(int,input().split())
  C = list(map(int,input().split()))
  s = 0
  for i in range(b):
    C[i] -=1 #oindex
    s = s|1<<C[i] #それぞれの宝箱の番号で左シフトしてorをとることでどの宝箱を開けられるかを保存。
  key.append((s,a)) #開けられる宝箱とコストを保存
#print(key)
INF = float("inf")  
dp = [INF for _ in range(1<<N)]
dp[0] = 0
#配るDP O(2^N*M)
for s in range(1<<N): #小さい順からやるとうまく遷移ができる。
  for i in range(M): #すべてのカギについて遷移を試す。
    t = s|key[i][0] #現在の宝箱の状態sに対して、新しい鍵を加えたときに開けられる宝箱の状態。 
    dp[t] = min(dp[t],dp[s] + key[i][1])
#print(dp)
if dp[-1] == INF:
  ans = -1
else:
  ans = dp[-1]
print(ans)
