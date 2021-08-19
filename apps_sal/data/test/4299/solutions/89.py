n = list(input())
a = int(n[len(n) - 1])
if a == 0 or a == 1 or a == 6 or (a == 8):
    print('pon')
elif a == 2 or a == 4 or a == 5 or (a == 7) or (a == 9):
    print('hon')
elif a == 3:
    print('bon')
