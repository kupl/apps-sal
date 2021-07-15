n = int(input())
for i in range(n - 1):
    if i % 2 == 0:
        print('I hate that ', end='')
    else:
        print('I love that ', end='')
if n % 2 == 0:
    print('I love it', end='')
else:
    print('I hate it', end='')
print()

