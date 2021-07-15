N = int(input())
t = list(map(int,input().split()))
v = list(map(int,input().split()))
T = sum(t)
ans = [0]

for i in range(N):
  ans[-1] = min(ans[-1],v[i])
  for j in range(t[i]*2):
    ans.append(v[i])

ans[-1] = 0

for i in range(2*T):
  ans[i+1]=min(ans[i]+0.5,ans[i+1])

for i in range(2*T,0,-1):
  ans[i-1]=min(ans[i]+0.5,ans[i-1])

print(sum(ans)/2)
