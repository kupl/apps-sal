S = input()
T = input()

lt = len(T)
ls = len(S)
if ls < lt:
    f = 0
else:
    for i in range(ls - lt, -1, -1):
        f = 1
        for s, t in zip(S[i:i + lt], T):
            if s == '?' or s == t:
                continue
            f = 0
        if f:
            break
print((S[0:i] + T + S[i + lt:ls]).replace('?', 'a') if f else 'UNRESTORABLE')
