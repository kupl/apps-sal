(n, k) = list(map(int, input().split()))
s = list(input()[::-1]) * 2
(ptn, win) = ('PR_RS_SP_RP_SR_PS_PP_RR_SS', 'PRS')
for _ in range(k):
    tmp = []
    while s:
        hand = ptn.index(s.pop() + s.pop())
        tmp.append(win[hand // 3 % 3])
    s = tmp[::-1] * 2
print(s.pop())
