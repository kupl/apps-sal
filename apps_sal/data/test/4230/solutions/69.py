X, N = list(map(int, input().split()))
flg = False
i = 1

if N == 0:
    Ans = X
else:
    S = list(map(int, input().split()))
    if X not in S:
        Ans = X
        flg = True

    while not flg:
        if X - i not in S:
            Ans = X - i
            flg = True
            break
        elif X + i not in S:
            Ans = X + i
            flg = True
            break
        else:
            i += 1

print(Ans)
