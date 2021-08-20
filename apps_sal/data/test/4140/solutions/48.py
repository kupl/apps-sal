s = list(input())
r1 = 0
r2 = 0
for (ii, ss) in enumerate(s):
    if ii % 2 == 0:
        if ss == '0':
            r1 += 1
        else:
            r2 += 1
    elif ss == '1':
        r1 += 1
    else:
        r2 += 1
print(min(r1, r2))
