N = int(input())
S1 = list(input())
S2 = list(input())
out = 1
i = 0
while i < N:
    if i == 0:
        if S1[i] == S2[i]:
            out *= 3
            flg = 0
        else:
            out *= 6
            flg = 1
            i += 1
    elif flg == 0:
        if S1[i] == S2[i]:
            out *= 2
            flg = 0
        else:
            out *= 2
            i += 1
            flg = 1
    elif S1[i] == S2[i]:
        out *= 1
        flg = 0
    else:
        out *= 3
        flg = 1
        i += 1
    i += 1
print(out % 1000000007)
