import sys
n = input()
koor = 1
summa = 0
for i in n:
    if (ord(i) - 96) == koor:
        summa += 0
    else:
        summa += min([abs(ord(i) - 96 - koor), 26 - abs(ord(i) - 96 - koor)])
        koor = ord(i) - 96
print(summa)
