N, M = map(int, input().split())
P_S = [input().split() for _ in range(M)]
wa_cnt = [0] * N
ac = 0
wa = 0
for p, s in P_S:
    index = int(p) - 1
    # ACの場合
    if s == "AC":
        # 初めてではない場合
        if wa_cnt[index] != -1:
            wa += wa_cnt[index]
            wa_cnt[index] = -1
            ac += 1
    else:
        if wa_cnt[index] != -1:
            wa_cnt[index] += 1

print(ac, wa)
