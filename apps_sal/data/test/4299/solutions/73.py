N = input()
if N[-1] == '2' or N[-1] == '4' or N[-1] == '5' or (N[-1] == '7') or (N[-1] == '9'):
    print('hon')
elif N[-1] == '0' or N[-1] == '1' or N[-1] == '6' or (N[-1] == '8'):
    print('pon')
else:
    print('bon')
