N = int(input())
shimo1keta = N % 10
if shimo1keta == 3:
    print('bon')
elif shimo1keta in [0, 1, 6, 8]:
    print('pon')
else:
    print('hon')
