t = int(input())
for i in range(t):
    s = input()
    m = len(s)
    x = int(input())
    ANS = [1] * m
    for i in range(m):
        if s[i] == '0':
            if i - x >= 0:
                ANS[i - x] = 0
            if i + x < m:
                ANS[i + x] = 0
    ng = 0
    for i in range(m):
        one = 0
        if i - x >= 0 and ANS[i - x] == 1 or (i + x < m and ANS[i + x] == 1):
            one = 1
        if one == 1 and s[i] == '0' or (one == 0 and s[i] == '1'):
            ng = 1
            break
    if ng == 1:
        print(-1)
    else:
        print(''.join([str(i) for i in ANS]))
