for i in range(int(input())):
    n = int(input())
    s = input()
    if s.find('8') != -1:
        k = s.find('8')
        if len(s) - k - 1 >= 10:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
