from itertools import product

N,A,B,C=map(int,input().split())
l = [int(input()) for _ in range(N)]

minscore=10**9
for p in product(range(-1,3),repeat=N):
  flag=0
  score = 0
  n_abc=[0,0,0]
  sumlen = [0,0,0]
  for i in range(N):
    if p[i] != -1:
      n_abc[p[i]] += 1
      sumlen[p[i]] += l[i]
  for j in range(3):
    if n_abc[j] == 0:
      flag=1
      break
    score += (n_abc[j]-1)*10 + abs(sumlen[j]-[A,B,C][j])
    
  if flag:
    continue
    
  if score < minscore:
    minscore = score
    
print(minscore)
