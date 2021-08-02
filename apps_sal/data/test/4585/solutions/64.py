x = int(input())
sn = 0
for i in range(1, 10 ** 5):
    sn = sn + i
    if sn >= x:
        print(i)
        break
