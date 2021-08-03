S = input()
T = input()

lt = len(T)
ls = len(S)
if ls < lt:
    flg = 0
else:
    for i in range(ls - lt, -1, -1):
        flg = 1
        for s, t in zip(S[i:i + lt], T):
            if s == '?' or s == t:
                continue
            flg = 0
        if flg:
            break
print((S[0:i] + T + S[i + lt:ls]).replace('?', 'a') if flg else 'UNRESTORABLE')
