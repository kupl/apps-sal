n = input()
if len(n) <= 7:
    if int(n) % 9 == 0:
        print('Yes')
    else:
        print('No')
else:
    sum = 0
    for i in n:
        sum = sum + int(i)
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')
