n = str(input())
n = int(n[-1])

if n in {3}:
    print('bon')
elif n in {0, 1, 6, 8}:
    print('pon')
else:
    print('hon')
