(a, b) = (int(x) for x in input().split())
multi = a * b
if multi % 2 == 0:
    print('Even')
else:
    print('Odd')
