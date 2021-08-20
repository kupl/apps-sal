n = input()
if n[-1] == '2' or n[-1] == '4' or n[-1] == '5' or (n[-1] == '7') or (n[-1] == '9'):
    print('hon')
elif n[-1] == '0' or n[-1] == '1' or n[-1] == '6' or (n[-1] == '8'):
    print('pon')
else:
    print('bon')
