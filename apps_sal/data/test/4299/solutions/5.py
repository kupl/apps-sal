N = int(input())
ans=N%10
if ans == 3:
    print('bon')
elif ans in [0, 1, 6, 8]:
    print('pon')
else:
    print('hon')
