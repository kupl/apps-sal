nn = list(str(input()))
n = [int(x) for x in nn]
a = [2, 4, 5, 7, 9]
b = [0, 1, 6, 8]
if n[-1] in a:
    print('hon')
elif n[-1] in b:
    print('pon')
elif n[-1] == 3:
    print('bon')
