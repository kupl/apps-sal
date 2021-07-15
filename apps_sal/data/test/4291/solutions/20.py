import sys

N, Q = map(int,input().split())
S = input()

cnt = [0]*(N+1)
wasA = False

for i in range(0,N):
  if wasA and S[i] == "C":
    cnt[i+1] = cnt[i] + 1
    wasA = False
  elif S[i] == "A":
    cnt[i+1] = cnt[i]
    wasA = True
  else:
    cnt[i+1] = cnt[i]
    wasA = False

#print(cnt)    

for i in range(0,Q):
  l, r = map(int,input().split())
  print(cnt[r]-cnt[l])
