N = int(input())
n = N % 10
if n in [2, 4, 5, 7, 9]:
    print('hon')
if n in [0, 1, 6, 8]:
    print('pon')
if n in [3]:
    print('bon')
