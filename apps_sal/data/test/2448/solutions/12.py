q = int(input())
for queries in range(q):
    n = int(input())
    (a, b, c) = list(map(int, input().split()))
    s = input()
    req = (n + 1) // 2
    s2 = []
    for i in s:
        if i == 'R':
            if b > 0:
                s2 += ['P']
                req -= 1
                b -= 1
            else:
                s2 += ['2']
        if i == 'P':
            if c > 0:
                s2 += ['S']
                req -= 1
                c -= 1
            else:
                s2 += ['3']
        if i == 'S':
            if a > 0:
                s2 += ['R']
                req -= 1
                a -= 1
            else:
                s2 += ['1']
    if req > 0:
        print('NO')
    else:
        print('YES')
        for i in range(n):
            if s2[i] == '1':
                if b > 0:
                    b -= 1
                    s2[i] = 'P'
                elif c > 0:
                    c -= 1
                    s2[i] = 'S'
            if s2[i] == '2':
                if a > 0:
                    a -= 1
                    s2[i] = 'R'
                elif c > 0:
                    c -= 1
                    s2[i] = 'S'
            if s2[i] == '3':
                if b > 0:
                    b -= 1
                    s2[i] = 'P'
                elif a > 0:
                    a -= 1
                    s2[i] = 'R'
        print(''.join(s2))
