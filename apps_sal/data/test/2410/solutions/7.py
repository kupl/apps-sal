test = int(input())
for z in range(test):
    amount = int(input())
    numb = list(map(int, input().split()))
    all = sum(numb)
    happy = True
    summ = 0
    for i in range(amount - 1):
        summ += numb[i]
        if summ <= 0:
            happy = False
            break
    if not happy:
        print('NO')
        continue
    else:
        summ = 0
        for i in range(amount - 1, 0, -1):
            summ += numb[i]
            if summ <= 0:
                happy = False
                break
        if not happy:
            print('NO')
            continue
    print('YES')
