N, T = map(int,input().split())
t_lis = list(map(int,input().split()))

ans = 0
for i in range(1,N):
  t = t_lis[i] - t_lis[i-1]
  ans += min(t, T)
  
print(ans + T)
