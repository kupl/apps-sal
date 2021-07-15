from math import gcd

t = int(input())
for q in range(t):
    nn = int(input())
    k, b, n = list(map(int, input().split()))
    s = input()
    w = 0
    aaa = [0] * nn
    for i in range(nn):
        if s[i] == 'R' and b:
            w += 1
            b -= 1
            aaa[i] = 'P'
        elif s[i] == 'P' and n:
            w += 1
            n -= 1
            aaa[i] = 'S'
        elif s[i] == 'S' and k:
            w += 1
            k -= 1
            aaa[i] = 'R'
    for i in range(nn):
        if type(aaa[i]) == int:
            if k:
                k -= 1
                aaa[i] = 'R'
            elif b:
                b -= 1
                aaa[i] = 'P'
            else:
                n -= 1
                aaa[i] = 'S'
    if nn // 2 + nn % 2 <= w:
        print('YES')
        print(''.join(aaa))
    else:
        print('NO')

