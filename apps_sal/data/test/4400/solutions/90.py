# SSS 0
# SSR 1
# SRS 1
# SRR 2
# RSS 1
# RSR 1
# RRS 2
# RRR 3
# 8toori


S = input()

cnt = 0
ans = 0

for i in range(len(S)):
    # range 回すたびに１つカウントが上がってiに代入される
    # len 文字数を数える
    if S[i] == 'R':
        cnt = cnt + 1
        if ans < cnt:
            ans = cnt
    else:
        cnt = 0

print(ans)
