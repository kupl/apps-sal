import math
l = int(input())
a = input()
l_a = len(a)
if l_a % l != 0:
    l_in_P = int(l_a / l) + 1
    i = 0
    P = 10 ** (l - 1)
    P = str(P)
    amount = 0
    while i < l_in_P:
        print(P, end='')
        i = i + 1
else:
    l_in_P = int(l_a / l)
    a_str = a
    int_for_P = a_str[0:l]
    compare = '='
    i = 0
    while i < l_in_P:
        index = l * i
        difference = int(a_str[index:index + l]) - int(int_for_P)
        if difference != 0:
            if difference < 0:
                compare = '<'
            else:
                compare = '>'
            break
        i = i + 1
    if compare == '<':
        i = 0
        while i < l_in_P:
            print(int_for_P, end='')
            i = i + 1
    elif int_for_P != '9' * l:
        P = int_for_P
        k = l - 1
        while P[k] == '9':
            k = k - 1
        P = P[0:k] + str(int(P[k]) + 1) + '0' * (l - k - 1)
        i = 0
        while i < l_in_P:
            print(P, end='')
            i = i + 1
    else:
        P = '1' + '0' * (l - 1)
        l_in_P = l_in_P + 1
        i = 0
        while i < l_in_P:
            print(P, end='')
            i = i + 1
