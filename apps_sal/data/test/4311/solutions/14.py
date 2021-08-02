s = int(input())
TMP = [s]

if s == 1 or s == 2:
    print(4)
else:
    while TMP[-1] != 1:
        if TMP[-1] % 2 == 0:
            TMP.append(TMP[-1] // 2)
        elif TMP[-1] % 2 != 0:
            TMP.append(3 * TMP[-1] + 1)
    print(len(TMP) + 1)
