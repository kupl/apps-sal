n = int(input())
print('I hate ', end='')
for i in range(1, n):
    if i % 2 == 0:
        print('that I hate ', end='')
    else:
        print('that I love ', end='')
print('it')
