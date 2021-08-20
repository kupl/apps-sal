for TT in range(1, int(input()) + 1):
    n = int(input())
    s = input()
    res = True
    if '8' not in s:
        res = False
    else:
        i = s.index('8')
        if n - i < 11:
            res = False
    print('YES' if res else 'NO')
