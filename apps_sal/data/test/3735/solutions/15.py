n = input()

if len(n) == 1:
    print(n)
else:
    if len([_ for _ in n if _ != '9']) == 0:
        a, b = n, '0'
    else:
        a = '9' * (len(n) - 1)
        b = str(int(n) - int(a))

    s = sum([int(_) for _ in a]) + sum([int(_) for _ in b])
    print(s)

