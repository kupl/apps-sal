N, T = map(int, input().split())
c = [0 for i in range(N)]
t = [0 for i in range(N)]
for i in range(N):
  c[i], t[i] = map(int, input().split())

ans = float('inf')
flag = False
for i in range(N):
  if t[i] <= T:
    flag = True
    if ans > c[i]:
      ans = c[i]
if flag:
  print(ans)
else:
  print('TLE')
