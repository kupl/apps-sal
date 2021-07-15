S = list(input())
N = len(S)
S.append('R')
ans = [0]*N

#cnt for RL
cnt = [0,0]
l = 'R'
for i in range(N):
  if S[i] == l:
    cnt[0] += 1
  elif S[i] == S[i+1]:
    cnt[1] += 1
  else:
    cnt[1] += 1
    r1 = cnt[0]//2
    r2 = cnt[1]//2
    ans[i-cnt[1]] = cnt[0] - r1 + r2
    ans[i-cnt[1]+1] = cnt[1] - r2 + r1
    cnt=[0,0]
print(' '.join(str(n) for n in ans))
