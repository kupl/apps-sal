n = int(input())
hon = [2, 4, 5, 7, 9]
pon = [0, 1, 6, 8]
num = n % 10
if num in hon:
    print('hon')
elif num in pon:
    print('pon')
elif num == 3:
    print('bon')
