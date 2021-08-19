t = int(input())
for i in range(t):
    s = input()
    if s[-1] == 'o':
        print('FILIPINO')
    elif s[-1] == 'u':
        print('JAPANESE')
    else:
        print('KOREAN')
