n = int(input())
if n == 1:
    if input() == '0':
        print('NO')
    else:
        print('YES')
else:
    sum = 0
    for s in input().split():
        if int(s) == 0:
            sum += 1
        if sum > 1:
            break
    if sum == 1:
        print('YES')
    else:
        print('NO')
        

