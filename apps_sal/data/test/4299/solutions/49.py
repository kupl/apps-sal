N = list(input())
if N[len(N) - 1] == '2' or N[len(N) - 1] == '4' or N[len(N) - 1] == '5' or (N[len(N) - 1] == '7') or (N[len(N) - 1] == '9'):
    print('hon')
elif N[len(N) - 1] == '0' or N[len(N) - 1] == '1' or N[len(N) - 1] == '6' or (N[len(N) - 1] == '8'):
    print('pon')
elif N[len(N) - 1] == '3':
    print('bon')
