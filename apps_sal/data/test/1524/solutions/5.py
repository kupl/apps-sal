from itertools import groupby
S = list(input())
Sl = len(S)
ans = [0]*Sl
RL = 0
count = -1
for _, v in groupby(S):
    x = list(v)
    xl = len(x)
    if RL == 0:
        count += xl
        if xl % 2 == 0:
            ans[count] += xl//2
            ans[count+1] += xl//2
        else:
            ans[count] += xl//2+1
            ans[count+1] += xl//2
        RL = 1
    else:
        if xl % 2 == 0:
            ans[count+1] += xl//2
            ans[count] += xl//2
        else:
            ans[count+1] += xl//2+1
            ans[count] += xl//2
        RL = 0
        count += xl
for i in ans:
    print(i, end=" ")

