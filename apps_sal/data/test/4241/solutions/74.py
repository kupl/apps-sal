S = input()
T = input()
lens = len(S)
lent = len(T)
mincnt = lent


if lens == lent:
    if S == T:
        mincnt = 0
    else:
        cnt = 0
        for i in range(lent):
            if S[i] != T[i]:
                cnt += 1
        mincnt = cnt
else:
    for i in range(lens - lent):
        cnt = 0
        for j in range(lent):
            if S[i + j] != T[j]:
                cnt += 1
        if cnt < mincnt:
            mincnt = cnt

print(mincnt)
