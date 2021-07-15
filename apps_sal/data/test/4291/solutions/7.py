N, Q = map(int, input().split())
S = input()
cnt = [0]*N
for i in range(N-1):
  T = S[i:i+2]
  if T == 'AC':
    cnt[i+1] = cnt[i] + 1
  else:
    cnt[i+1] = cnt[i]
for i in range(Q):
  x, y = map(int, input().split())
  ans = cnt[y-1]-cnt[x-1]
  print(ans)
