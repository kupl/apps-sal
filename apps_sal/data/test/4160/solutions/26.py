x = int(input())
yen = 100
cnt = 0
while yen < x:
    yen = yen * 101 // 100
    cnt += 1
print(cnt)
