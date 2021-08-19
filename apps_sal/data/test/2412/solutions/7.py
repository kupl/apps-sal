for _ in range(int(input())):
    input()
    num = input()
    if '8' in num and len(num) - num.find('8') >= 11:
        print('YES')
    else:
        print('NO')
