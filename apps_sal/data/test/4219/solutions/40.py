n = int(input())
xy = [[] for i in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x,y = map(int, input().split())
        xy[i].append((x,y))

ans = 0
for i in range(2**n):
    isOk = True
    res = []
    cnt = 0
    for j in range(n) :
        x = i >> j & 1
        res.append(x)
    for j in range(n):
        x = i >> j & 1
        if(x):
            cnt += 1
            for v in xy[j] :
                x,y = v
                x -= 1
                if(res[x] != y):
                    isOk = False
    if(isOk):
        ans = max(ans, cnt)  
print(ans)
