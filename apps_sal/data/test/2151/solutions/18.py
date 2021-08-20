for i in range(int(input())):
    n = int(input())
    s = input()
    if len(s) > 2:
        print('YES')
        print(2)
        print(s[0], s[1:])
    elif len(s) == 1 or s[0] >= s[1]:
        print('NO')
    else:
        print('YES')
        print(2)
        print(s[0], s[1:])
