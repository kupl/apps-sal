n = int(input())
print('I hate ', end='')
for i in range(1, n):
    if i % 2 == 1:
        print('that I love ', end='')
    else:
        print('that I hate ', end='')
print('it')
