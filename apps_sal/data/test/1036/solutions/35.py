n, k = list(map(int, input().split()))
s = list(input()[::-1]) * 2

ptn, win = 'PR_RP_PP_RS_SR_RR_SP_PS_SS', 'PRS'
for _ in range(k):
    tmp = []
    while s:
        hand = ptn.index(s.pop() + s.pop())
        tmp.append(win[hand // 9])
    s = tmp[::-1] * 2
print((s.pop()))

