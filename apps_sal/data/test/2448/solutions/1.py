t = int(input())

for _ in range(t):
    n = int(input())
    a,b,c = list(map(int,input().split()))
    ss = input()
    r,p,s = ss.count('R'),ss.count('P'),ss.count('S')
    win = min(a, s) + min(b, r) + min(c, p)
    if win < (n + 1) // 2:
        print('NO')
        continue
    print('YES')
    res = ['' for i in range(n)]
    for i in range(n):
        if ss[i] == 'R' and b > 0:
            res[i] = 'P'
            b -= 1
        if ss[i] == 'P' and c > 0:
            res[i] = 'S'
            c -= 1
        if ss[i] == 'S' and a > 0:
            res[i] = 'R'
            a -= 1
    for i in range(n):
        if res[i] == '':
            if a:
                res[i] = 'R'
                a -= 1
            elif b:
                res[i] = 'P'
                b -= 1
            elif c:
                res[i] = 'S'
                c -= 1
    print(''.join(res))

