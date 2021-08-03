for _ in range(int(input())):
    s = input()
    one = s.count('1')
    zero = s.count('0')
    total = min(one, zero)
    if total % 2 == 1:
        print('DA')
    else:
        print('NET')
