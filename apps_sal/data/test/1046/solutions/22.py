input()
lst = list(map(int, input().split()))

dct = {}
for i in lst:
    if i > 0:
        dct[i] = dct.get(i, 0) + 1

total = 0
for v in list(dct.values()):
    if v == 2:
        total += 1
    elif v > 2:
        total = -1
        break

print(total)
