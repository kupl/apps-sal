d, g = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(d)]

ans = 100*11
for i in range(2**d):
    sum = 0
    cnt = 0
    a = []
    for j in range(d):
        if (i >> j) & 1 == 1:
            sum += (j+1)*100*pc[j][0] + pc[j][1]
            cnt += pc[j][0]
            a.append(j)
    if sum < g:
        for j in range(d):
            if d-j-1 not in a:
                for k in range(pc[d-j-1][0]):
                    if sum >= g:
                        break
                    sum += (d-j)*100
                    cnt += 1
    ans = min(ans, cnt)
print(ans)
