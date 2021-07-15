n = int(input())
p = list(map(int,input().split()))
ans = [i for i in range(1,n+1)]
cnt = 0
 
for i in range(n):
  if p[i] != ans[i]:
    cnt += 1
  if cnt > 2:
    print('NO')
    return
    
print('YES')
