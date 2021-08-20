def digit(n2):
    if n2 == 1:
        print('-one')
    elif n2 == 2:
        print('-two')
    elif n2 == 3:
        print('-three')
    elif n2 == 4:
        print('-four')
    elif n2 == 5:
        print('-five')
    elif n2 == 6:
        print('-six')
    elif n2 == 7:
        print('-seven')
    elif n2 == 8:
        print('-eight')
    elif n2 == 9:
        print('-nine')


n = int(input())
n1 = n // 10
n2 = n % 10
if n1 == 0:
    if n2 == 0:
        print('zero')
    elif n2 == 1:
        print('one')
    elif n2 == 2:
        print('two')
    elif n2 == 3:
        print('three')
    elif n2 == 4:
        print('four')
    elif n2 == 5:
        print('five')
    elif n2 == 6:
        print('six')
    elif n2 == 7:
        print('seven')
    elif n2 == 8:
        print('eight')
    elif n2 == 9:
        print('nine')
elif n1 == 1:
    if n2 == 0:
        print('ten')
    elif n2 == 1:
        print('eleven')
    elif n2 == 2:
        print('twelve')
    elif n2 == 3:
        print('thirteen')
    elif n2 == 4:
        print('fourteen')
    elif n2 == 5:
        print('fifteen')
    elif n2 == 6:
        print('sixteen')
    elif n2 == 7:
        print('seventeen')
    elif n2 == 8:
        print('eighteen')
    elif n2 == 9:
        print('nineteen')
elif n1 == 2:
    print('twenty', end='')
    digit(n2)
elif n1 == 3:
    print('thirty', end='')
    digit(n2)
elif n1 == 4:
    print('forty', end='')
    digit(n2)
elif n1 == 5:
    print('fifty', end='')
    digit(n2)
elif n1 == 6:
    print('sixty', end='')
    digit(n2)
elif n1 == 7:
    print('seventy', end='')
    digit(n2)
elif n1 == 8:
    print('eighty', end='')
    digit(n2)
elif n1 == 9:
    print('ninety', end='')
    digit(n2)
