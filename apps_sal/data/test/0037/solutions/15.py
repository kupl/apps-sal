__author__ = 'Utena'
a, b, c = map(int, map(int, input().split()))
while True:
    if c < 0:
        print('No')
        break
    elif c % a == 0 or c % b == 0:
        print('Yes')
        break
    c -= a
