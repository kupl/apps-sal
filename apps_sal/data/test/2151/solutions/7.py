n = int(input())
for _ in range(n):
    d = int(input())
    s = input()
    if len(s) == 1:
        print('NO')
    elif len(s) == 2:
        if s[0] < s[1]:
            print('YES')
            print(2)
            print(s[0], s[1:])
        else:
            print('NO')
    else:
        print('YES')
        print(2)
        print(s[0], s[1:])
