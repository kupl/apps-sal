n = list(input())

i = len(n) - 1

if n[i] == '3':
    print('bon')
elif n[i] == '0' or n[i] == '1' or n[i] == '6' or n[i] == '8':
    print('pon')
else:
    print('hon')
