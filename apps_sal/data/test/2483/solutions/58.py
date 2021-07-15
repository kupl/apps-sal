# ある時点の重複番組数を前からカウントして、最大値が答え
# s順に並べて、ループごとに重複数を増やしつつ、
# 終了キューにtを追加
# 番組追加するごとに終了キューの中身をチェック
# 同じチャンネルだったら、終了キューt <= 現在時刻 のときに終了キューから外せる
# 違うチャンネルだったら、終了キューt < 現在時刻となる
# チャンネルごとにheapqを持つ

N,C = map(int,input().split())
import heapq
endq = [[] for i in range(C)]
for i in range(C):
  heapq.heapify(endq[i])
progs = [None] * N
for i in range(N):
  s,t,c = map(int,input().split())
  progs[i] = [s,t,c-1]

progs = sorted(progs,key = lambda x:x[0])

ans = 0
cur = 0

for i in range(N):
  s,t,c = progs[i]
  # 時刻sに終了する番組をチェックする
  # まず同チャンネルのものが時刻sに終了していたら、それを外すことが出来る
  while endq[c]:
    endt = heapq.heappop(endq[c])
    if endt <= s:
      cur -= 1
    else:
      heapq.heappush(endq[c],endt)
      break
  
  # 他のチャンネルをチェックする
  for endc in range(C):
    if endc == c:
      continue # 同じチャンネルはチェック済み
    while endq[endc]:
      endt = heapq.heappop(endq[endc]) # 各チャンネルのキューから取り出す
      if endt < s:
        cur -= 1
      else:
        heapq.heappush(endq[endc],endt)
        break
  # 今回の番組を格納する
  cur += 1
  heapq.heappush(endq[c],t)
  if cur > ans:
    ans = cur

print(ans)
