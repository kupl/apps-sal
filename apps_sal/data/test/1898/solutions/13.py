n = int(input())
for i in range(n - 1):
    if i & 1:
        print('I love that ', end='')
    else:
        print('I hate that ', end='')
if n - 1 & 1:
    print('I love it')
else:
    print('I hate it')
