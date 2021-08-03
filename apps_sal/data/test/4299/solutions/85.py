N = input()
A = int(N[-1])
if A == 3:
    print('bon')
elif A == 0 or A == 1 or A == 6 or A == 8:
    print('pon')
else:
    print('hon')
