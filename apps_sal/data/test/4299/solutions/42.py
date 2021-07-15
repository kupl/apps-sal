N = int(input())

if str(N)[-1] == str(3):
    print('bon')
elif str(N)[-1] in list(map(str, [0, 1, 6, 8])):
    print('pon')
else:
    print('hon')
