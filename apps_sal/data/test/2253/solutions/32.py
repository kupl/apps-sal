t = int(input())
for i in range(t):
    a = input()
    if a[-2:] == 'po':
        print('FILIPINO')
    elif a[-4:] == 'desu' or a[-4:] == 'masu':
        print('JAPANESE')
    elif a[-5:] == 'mnida':
        print('KOREAN')
