k = int(input())
lun = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
while len(lun) < k:
    if lun[i] % 10 == 0:
        lun.append(lun[i] * 10 + lun[i] % 10 - 0)
        lun.append(lun[i] * 10 + lun[i] % 10 + 1)
    elif lun[i] % 10 == 9:
        lun.append(lun[i] * 10 + lun[i] % 10 - 1)
        lun.append(lun[i] * 10 + lun[i] % 10 - 0)
    else:
        lun.append(lun[i] * 10 + lun[i] % 10 - 1)
        lun.append(lun[i] * 10 + lun[i] % 10 - 0)
        lun.append(lun[i] * 10 + lun[i] % 10 + 1)
    i += 1
print(lun[k-1])
