N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

# 愚直に考えるとO(QN)で間に合わないので、以下のような操作に置き換える
# 開始時点の全員のポイントはK-Qとする
# Q回の正解それぞれに対し、正解者のポイントを1増やす
# するとO(Q+N)で解け、間に合う
p = [K-Q]*N
for i in range(Q):
  p[A[i]-1] += 1
  
for i in range(N):
  if p[i] > 0: print('Yes')
  else: print('No')
