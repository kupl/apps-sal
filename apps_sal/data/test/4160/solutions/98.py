yen = 100
X = int(input())
count = 0
while True:
    i = yen // 100
    yen = yen + i
    count = count + 1
    if yen >= X:
        print(count)
        break
