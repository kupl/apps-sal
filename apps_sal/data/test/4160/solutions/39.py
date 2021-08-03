x = int(input())
cnt = 0
yen = 100

while yen < x:
    yen += yen // 100
    cnt += 1

print(cnt)
