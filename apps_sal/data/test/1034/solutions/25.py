from heapq import *

X,Y,Z,K = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

# Heapq的なのでぶっこみPopしてればよい
# そのかわり全パターン最初からぶち込むのはむりなので、popしたindexをもとに候補となる対象をpushする必要がある
# ただし容易に重複投入しうるので、投入済みパターンを覚えておくのかな…。historyに含まれてたらSKIP。
Q = []
his = set()

def pushq(p,q,r):
  if (p,q,r) in his:
    return
  if p >= X or q >= Y or r >= Z:
    return
  his.add((p,q,r))
  heappush(Q, ((-1) * (A[p] + B[q] + C[r]), (p, q, r)))
  return

pushq(0,0,0)
for _ in range(K):
  V = heappop(Q)
  print(((-1)*V[0]))
  p,q,r = V[1]
  pushq(p+1,q,r)
  pushq(p,q+1,r)
  pushq(p,q,r+1)
  

