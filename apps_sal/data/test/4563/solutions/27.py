N = int(input())
Q = [tuple(map(int, input().split())) for _ in range(N)]
vote = Q[0]  # 初期値はそのまま得票(互いに素)

for p, q in Q[1:]:
    if p == q:
        g = max(vote)
        vote = (g, g)
    # p基準: 現在の得票以上の最小のpの倍数
    p_v0 = ((vote[0] + p - 1) // p) * p
    p_v1 = q * p_v0 // p
    # q基準
    q_v1 = ((vote[1] + q - 1) // q) * q
    q_v0 = p * q_v1 // q
    # 減っていたら除外
    if p_v1 < vote[1]:
        vote = (q_v0, q_v1)
    elif q_v0 < vote[0]:
        vote = (p_v0, p_v1)
    else:
        # どっちもありえるなら小さいほう
        if p_v0 + p_v1 <= q_v0 + q_v1:
            vote = (p_v0, p_v1)
        else:
            vote = (q_v0, q_v1)

ans = sum(vote)
print(ans)
