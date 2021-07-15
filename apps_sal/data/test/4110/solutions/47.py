from math import ceil

D, G = map(int,input().split())
pc = [list(map(int,input().split())) for i in range(D)]

ans = float("inf")
for bit in range(1 << D):
    cnt = 0
    sum = 0
    remain = set(range(1,D+1))

    for i in range(D):
        if bit & (1 << i):
            cnt += pc[i][0]
            sum += pc[i][0]*(i+1)*100 + pc[i][1]
            remain.discard(i+1)

    if sum < G:
        use = max(remain)
        n = min(pc[use-1][0], ceil((G-sum)/(use*100)))
        cnt += n
        sum += n*use*100

    if sum >= G:
        ans = min(ans,cnt)

print(ans)
