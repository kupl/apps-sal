a = list(map(int, input().split()))
b = a[1]
a = a[0]
i = 0
while i < a:
    if i % 4 == 0 or i % 4 == 2:
        print('
    if i % 4 == 1:
        print((b - 1) * '.' + '
    if i % 4 == 3:
        print('
    i=i + 1
