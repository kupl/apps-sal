getints = lambda: list(map(int, input().split()))
a, b = getints()
if a * b % 2:
    print('Odd')
else:
    print('Even')

