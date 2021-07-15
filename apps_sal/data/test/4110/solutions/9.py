D, G = list(map(int, input().split())) #D: 問題数, G: 目標点
PC = [list(map(int, input().split())) for i in range(D)]

ans = float("inf")

for i in range(2**D):
    tmp = 0
    cnt = 0
    dic = set(range(1, D+1))
    for j in range(D):
        if (i >> j)&1: #その問題は全て解く
            tmp += PC[j][0] * (j+1) * 100 + PC[j][1]
            cnt += PC[j][0]
            dic.discard(j+1)

    if tmp < G:
        t = max(dic)
        p, c = PC[t-1][0], PC[t-1][1]
        if t*100*p+c+tmp >= G:
            while p:
                tmp += t*100
                cnt += 1
                if tmp >= G:
                    break
            ans = min(ans, cnt)
    else:
        ans = min(ans, cnt)
print(ans)

