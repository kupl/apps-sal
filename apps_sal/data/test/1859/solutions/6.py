n = int(input())
count = 0
while n != 0:
    if n % 2 == 0:
        count += n // 2
        break
    flag = 0
    for i in range(2, int(n ** 0.5 + 100)):
        if n % i == 0:
            flag = 1
            break
    count += 1
    if flag == 0:
        break
    else:
        n -= i
print(count)
