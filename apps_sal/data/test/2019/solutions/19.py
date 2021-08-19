for _ in range(int(input())):
    s = input()
    a = s.count('1')
    b = s.count('0')
    x = min(a, b)
    if x % 2 == 1:
        print('DA')
    else:
        print('NET')
