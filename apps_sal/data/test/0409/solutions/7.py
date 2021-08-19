def __starting_point():
    s = input()
    a = None
    b = None
    for i in range(len(s) - 1):
        if s[i] == 'A' and s[i + 1] == 'B':
            if a is None:
                a = i
            if b is not None and abs(i - b) > 1:
                print('YES')
                return
        if s[i] == 'B' and s[i + 1] == 'A':
            if b is None:
                b = i
            if a is not None and abs(a - i) > 1:
                print('YES')
                return
    print('NO')


__starting_point()
