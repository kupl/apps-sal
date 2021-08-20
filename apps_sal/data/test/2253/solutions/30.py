for _ in range(int(input())):
    s = input()
    if s[-2:] == 'po':
        print('FILIPINO')
    elif s[-4:] == 'masu' or s[-4:] == 'desu':
        print('JAPANESE')
    else:
        print('KOREAN')
