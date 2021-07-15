N, K = map(int, input().split())
mod = 1000000007

E = [[] for i in range(N)]
for i in range(N-1):
  a, b = map(int, input().split())
  E[a-1].append(b-1)
  E[b-1].append(a-1)
#ここまでで木をリスト化

counts = [False]*N
#各々の頂点について1回ずつ考えるようにTrueになったら進行しないようにコマンド
q = [0]
counts[0] = True
ans = K
while q:
  i = q.pop(0)
  # get_nexts
  js = E[i]
  if i == 0:
    c = K - 1
  else:
    c = K - 2
  for j in js:
    if not(counts[j]):
      counts[j] = True
      ans = (ans * c) % mod
      c -= 1
      q.append(j)
#print(E)      
print(ans)
