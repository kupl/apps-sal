N = int(input())
N = N % 10
if N == 2 or N == 4 or N == 5 or N == 7 or N == 9:
    print('hon')
elif N == 3:
    print('bon')
else:
    print('pon')
