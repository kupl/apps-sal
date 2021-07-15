X = int(input())
yen = 100
count = 0

while yen < X:
    yen = (yen * 101) // 100
    count += 1

print(count)
