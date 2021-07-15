a, b = map(int, input().split())
if b - a == 1:
    print(a, b)
elif a == b:
    print(a, '0 ', b, '1', sep='')
elif b == 1 and a == 9:
    print(9, 10)
else:
    print('-1')
