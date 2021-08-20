for _ in range(int(input())):
    a = input()
    b = input()
    c = input()
    n = len(a)
    flag = 0
    for i in range(n):
        if a[i] == c[i] or b[i] == c[i]:
            continue
        flag = 1
        break
    if flag == 0:
        print('YES')
    else:
        print('NO')
