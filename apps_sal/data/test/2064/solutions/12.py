a = int(input())
if a % 2:
    print('7', end='')
    a -= 3
while a > 0:
    a -= 2
    print('1', end='')
