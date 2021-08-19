s = int(input())
a = [0, 1, 6, 8]
b = [3]
if s % 10 in a:
    print('pon')
elif s % 10 in b:
    print('bon')
else:
    print('hon')
