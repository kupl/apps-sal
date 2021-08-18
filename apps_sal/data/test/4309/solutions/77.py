a = input()
zyun = len(a) * 9 + int(a[0])
zoro = 0
z = zyun // 9
af = zyun % 9
if af == 0:
    if int(a) <= int(str(9) * (z - 1)):
        print((int(str(9) * (z - 1))))
    else:
        print((str(1) * (z)))
else:
    if int(a) <= int(str(af) * (z)):
        print((int(str(af) * (z))))
    else:
        print((int(str(af + 1) * (z))))
