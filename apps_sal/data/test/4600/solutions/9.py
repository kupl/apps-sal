N, M = map(int, input().split())
p_S = [input().split() for _ in range(M)]

# N, M=O(10^5)なので、O(N+M)で解く！
AC = [False]*N
WA = [0]*N
 
# i番目の提出において、
# (1) まだ'AC'されておらず、提出がWAだった場合：WA += 1
# (2) まだ'AC'されておらず、提出がACだった場合：AC += 1 
# (3) すでに'AC'されている場合：何もしない
for i in range(M):    
  num = int(p_S[i][0])-1
  if AC[num] == 0 and p_S[i][1] == 'WA': WA[num] += 1
  elif AC[num] == 0 and p_S[i][1] == 'AC': AC[num] = True
  else: continue

# 'AC'を出した各問題において、初めて'AC'を出すまでに出した'WA'の数の和を求める
s = 0
for i in range(N):
  if AC[i]:
    s += WA[i]
    
print(sum(AC), s)
