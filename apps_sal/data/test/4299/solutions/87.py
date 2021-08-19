n = list(input())
num = [0, 1, 6, 8]
if int(n[-1]) == 3:
    print('bon')
elif int(n[-1]) in num:
    print('pon')
else:
    print('hon')
