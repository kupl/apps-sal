n = int(input())
m = []
a = [[] for i in range(n)]
for i in range(n):
    tmp = int(input())
    m.append(tmp)
    for j in range(tmp):
        a[i].append(list(map(int,input().split())))

ans = 0

for i in range(2**n):
    cnt = 0
    for j in range(n):
        flg = True
        if i >> j & 1:
            cnt += 1
            for k in range(m[j]):
                kj = (i >> (a[j][k][0]-1)) & 1
                if a[j][k][1] != kj:
                    flg = False
                    break
            if not flg:
                break
    if flg:
        ans = max(ans, cnt)

print(ans)  

