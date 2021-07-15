n = int(input())
for i in range(n):
    print('NO' if 360 % (180 - int(input())) else 'YES')
