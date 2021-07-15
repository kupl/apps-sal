n = int(input())
q = [int(input())  for i in range(n)]
cnt = 0
ind = 0
for i in range(n):
    ind = q[ind]-1
    cnt += 1
    if ind == 1:
        print(cnt)
        return
    
print(-1)
