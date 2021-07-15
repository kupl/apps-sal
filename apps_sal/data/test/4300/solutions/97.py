N = int(input())
d = list(map(int, input().split()))

# 全探索する
ans = 0
for i in range(N):
  for j in range(i+1, N):
    ans += d[i]*d[j]
    
print(ans)
