X = int(input())
mon = 100
count = 0
while mon < X:
    mon += mon // 100
    count += 1
print(count)
