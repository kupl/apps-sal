n = list(input())
n = list(map(int, n))
if n[-1] == 3:
    print('bon')
elif n[-1] == 0 or n[-1] == 1 or n[-1] == 6 or n[-1] == 8:
    print('pon')
else:
    print('hon')
