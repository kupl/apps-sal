for _ in range(int(input())):
    N = int(input())
    s = input()

    if len(s) == 1:
        print('NO')
    elif len(s) == 2:
        if s[0] < s[1]:
            print('YES\n2\n' + s[0] + ' ' + s[1])
        else:
            print('NO')
    else:
        print('YES\n2\n' + s[0] + ' ' + s[1:])
