n = int(input())
n -= 1
print('I hate', end=' ')
n2 = 1
while n > 0:
    if n2 == 0:
        print('that I hate', end=' ')
        n2 = 1
    else:
        print('that I love', end=' ')
        n2 = 0
    n -= 1
print('it')
