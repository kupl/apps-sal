n,K = map(int,input().split())
d = [[int(i) for i in input().split()] for _ in range(n)]
x = sorted(d,key=lambda x:x[0])
y = sorted(d,key=lambda x:x[1])
ans = float("inf")

for i in range(n):
    for j in range(i+1,n):
        for k in range(n):
            cnt = 0
            for l in range(k,n):
                if x[i][0] <= y[l][0] <= x[j][0]: cnt += 1
                if cnt == K:
                    dx = x[j][0]-x[i][0]
                    dy = y[l][1]-y[k][1]
                    ans = min(ans, dx*dy)
                    break
print(ans)
