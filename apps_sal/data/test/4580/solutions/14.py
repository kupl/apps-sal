N = int(input())
A = list(map(int, input().split()))
cnt = [0] * 8
c = 0
for a in A:
    if a <= 399:
        cnt[0] += 1
    elif a >= 400 and a <= 799:
        cnt[1] += 1
    elif a >= 800 and a <= 1199:
        cnt[2] += 1
    elif a >= 1200 and a <= 1599:
        cnt[3] += 1
    elif a >= 1600 and a <= 1999:
        cnt[4] += 1
    elif a >= 2000 and a <= 2399:
        cnt[5] += 1
    elif a >= 2400 and a <= 2799:
        cnt[6] += 1
    elif a >= 2800 and a <= 3199:
        cnt[7] += 1
    else:
        c += 1
Min = len([i for i in cnt if i != 0])
if c == 0:
    print(Min, Min)
else:
    Max = Min + c
    if Min == 0:
        print(1, Max)
    else:
        print(Min, Max)
