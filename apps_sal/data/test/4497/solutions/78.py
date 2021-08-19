N = int(input())
count_max = -1
OK = True
for i in range(N):
    count = 0
    a = N - i
    while a % 2 == 0:
        a = a // 2
        count += 1
        if count_max < count:
            count_max = count
    else:
        continue
if 2 ** count_max == 0.5:
    print(1)
else:
    print(2 ** count_max)
