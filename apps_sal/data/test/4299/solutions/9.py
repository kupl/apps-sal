N = int(input())
X = (N % 100) % 10
if X == 3:
    print('bon')
elif X == 0 or X == 1 or X == 6 or X == 8:
    print('pon')
else:
    print('hon')
