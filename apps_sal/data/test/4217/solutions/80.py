n, m = map(int, input().split())
KA = [list(map(int, input().split())) for _ in range(n)]

ans = [0] * m

for i in range(n):
    A = KA[i][1:]
    for a in A:
        ans[a-1] += 1
        
cnt = 0
for a in ans:
  if a == n:
    cnt += 1
print(cnt)
