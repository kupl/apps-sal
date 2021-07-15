N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = T
for i in range(N-1):
  if t[i] + T <= t[i+1]:
    ans += T
  else:
    ans += t[i+1] - t[i] 
print(ans)
