S = input()
T = input()

lt = len(T)
ls = len(S)
if ls < lt: flg = 0
else:
    for i in range(ls - lt, -1, -1):
        flg = 1
        for j in range(i, i + lt):
            s = S[j]
            if s == '?' or s == T[j - i]: continue
            flg = 0
            break
        if flg: break
if flg:
    print((S[0:i] + T + S[i + lt:ls]).replace('?', 'a'))
else:
    print('UNRESTORABLE')
