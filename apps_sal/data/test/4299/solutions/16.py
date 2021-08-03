n = list(str(input()))
if n[-1] == '3':
    print('bon')
    return
if n[-1] == '0' or n[-1] == '1' or n[-1] == '6' or n[-1] == '8':
    print('pon')
    return
print('hon')
