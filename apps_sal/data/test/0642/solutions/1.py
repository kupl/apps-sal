N, M = list(map(int, input().split()))
if M > 0:
    Dirty = list(sorted((list(map(int, input().split())))))
    Flag = Dirty[0] != 1 and Dirty[-1] != N
    if Flag:
        Last = Dirty[0]
        Amount = 1
        for Num in Dirty:
            if Last + 1 == Num:
                Amount += 1
            else:
                Amount = 1
            Last = Num
            if Amount == 3:
                Flag = False
                break
    if Flag:
        print("YES")
    else:
        print("NO")
else:
    print("YES")
