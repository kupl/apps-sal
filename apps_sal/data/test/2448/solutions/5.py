for i in range(int(input())):
    n = int(input())
    a, b, c = list(map(int, input().split()))
    s = input()
    res = [''] * n
    w = 0
    for j in range(n):
        if s[j] == 'R' and b:
            b -= 1
            res[j] = 'P'
            w += 1
        elif s[j] == 'P' and c:
            c -= 1
            res[j] = 'S'
            w += 1
        elif s[j] == 'S' and a:
            a -= 1
            res[j] = 'R'
            w += 1
    for j in range(n):
        if res[j] == '':
            if a:
                res[j] = 'R'
                a -= 1
            elif b:
                res[j] = 'P'
                b -= 1
            elif c:
                res[j] = 'S'
                c -= 1
    if w >= (n + 1) // 2:
        print("YES")
        print(''.join(res))
    else:
        print("NO")
