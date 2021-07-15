n = int(input())
while n:
    x = input()
    if x[-2:] == 'po':
        print('FILIPINO')
    elif x[-4:] == 'masu' or x[-4:] == 'desu':
        print('JAPANESE')
    else:
        print('KOREAN')
    n -= 1
