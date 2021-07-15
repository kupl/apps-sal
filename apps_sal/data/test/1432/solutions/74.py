n = int(input())
a = list(map(int,input().split()))
ans = []
cnt = 0
for i in range(1,n-1,2):
  cnt += a[i]*2  
ans.append(sum(a)-cnt)
for i in range(n):
  ans.append(a[i]*2-ans[i])
print(*ans[:-1])
