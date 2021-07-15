D, G = map(int, input().split())

PC = [list(map(int, input().split())) for _ in range(D)]

ans = 10**9
for bit in range(2**D):
    cnt = 0
    score = 0
    dic = set(range(D))
    for i in range(D):
        if (bit>>i)&1:
            score += PC[i][0] * 100 * (i+1) + PC[i][1]
            cnt += PC[i][0]
            dic.discard(i)

    if score < G:
        t = max(dic)
        p, c = PC[t][0], PC[t][1]
        if (t+1)*100*p+c+score >= G:
            while p:
                score += (t+1)*100
                cnt += 1
                p -= 1
                if score >= G:
                    break
            ans = min(ans, cnt)
    else:
        ans = min(ans, cnt)
print(ans)
