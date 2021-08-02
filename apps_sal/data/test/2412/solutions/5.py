for i in range(int(input())):
    n = int(input())
    s = input().strip()
    k = s.find('8')
    if k == -1:
        print('NO')
        continue
    s = s[k:]
    if len(s) >= 11:
        print('YES')
    else:
        print('NO')
