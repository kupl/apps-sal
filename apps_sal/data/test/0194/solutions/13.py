n, a, b = list(map(int, input().strip().split(' ')))
P = list(map(int, input().strip().split(' ')))
count1 = 0
count2 = 0
count2half = 0
bad = 0
for i in range(len(P)):
    if P[i] == 1:
        if count1 < a:
            count1 += 1
        elif count2 < b:
            if 1 == 1:
                count2half += 1
                count2 += 1

        elif count2half > 0:
            count2half -= 1
        else:
            bad += 1

    else:
        if count2 < b:
            count2 += 1
        else:
            bad += 2
print(bad)
