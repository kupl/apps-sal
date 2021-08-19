str = input()
flg = False
count = 0
max = 0
for s in str:
    if s == 'R':
        if flg == True:
            count += 1
            if max < count:
                max = count
        else:
            flg = True
            count += 1
            if max < count:
                max = count
    else:
        flg = False
        count = 0
print(max)
