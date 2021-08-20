n = int(input())
for _ in range(n):
    s = input()
    if len(s) >= 2 and s[-2:] == 'po':
        print('FILIPINO')
    elif len(s) >= 4 and s[-4:] == 'desu':
        print('JAPANESE')
    elif len(s) >= 4 and s[-4:] == 'masu':
        print('JAPANESE')
    else:
        print('KOREAN')
