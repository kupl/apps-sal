(N, M) = map(int, input().split())
P_S = [input().split() for _ in range(M)]
wa_cnt = [0] * N
ac = 0
wa = 0
for (p, s) in P_S:
    index = int(p) - 1
    if s == 'AC':
        if wa_cnt[index] != -1:
            wa += wa_cnt[index]
            wa_cnt[index] = -1
            ac += 1
    elif wa_cnt[index] != -1:
        wa_cnt[index] += 1
print(ac, wa)
