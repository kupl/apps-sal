"""T=int(input())
for _ in range(0,T):
    N=int(input())
    a,b=map(int,input().split())
    s=input()
    s=[int(x) for x in input().split()]
    for i in range(0,len(s)):
        a,b=map(int,input().split())"""
T = int(input())
for _ in range(0, T):
    N = int(input())
    (a, b, c) = list(map(int, input().split()))
    s = input()
    ct = 0
    ans = ''
    for i in range(0, len(s)):
        if s[i] == 'R':
            if b > 0:
                b -= 1
                ans += 'P'
                ct += 1
            else:
                ans += '.'
        elif s[i] == 'P':
            if c > 0:
                c -= 1
                ans += 'S'
                ct += 1
            else:
                ans += '.'
        elif a > 0:
            a -= 1
            ans += 'R'
            ct += 1
        else:
            ans += '.'
    tg = N // 2
    if N % 2 != 0:
        tg += 1
    if ct >= tg:
        print('YES')
        ans1 = []
        for i in range(0, len(ans)):
            ans1.append(ans[i])
        for i in range(0, len(ans1)):
            if ans1[i] == '.':
                if a > 0:
                    ans1[i] = 'R'
                    a -= 1
                elif b > 0:
                    ans1[i] = 'P'
                    b -= 1
                elif c > 0:
                    ans1[i] = 'S'
                    c -= 1
        fnl = ''.join(ans1)
        print(fnl)
    else:
        print('NO')
