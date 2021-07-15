# n, x, a, b = map(int, input().split())

t = int(input())
for i in range(t):
    s = input()
    suff = s[-2:]
    if suff == 'po':
        print('FILIPINO')
    if suff == 'su':
        print('JAPANESE')
    if suff == 'da':
        print('KOREAN')


