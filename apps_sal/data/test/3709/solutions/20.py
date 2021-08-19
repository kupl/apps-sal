(n, k) = [int(i) for i in input().split()]
if k == 1:
    alert = 0
    for time in range(n):
        term = str(input())
        if term == '0':
            alert = 1
            break
    print('NO') if alert == 0 else print('YES')
elif k == 2:
    (s1, s2) = (0, 0)
    for time in range(n):
        term = str(input())
        if term == '0 0':
            (s1, s2) = (1, 1)
            break
        elif term == '0 1':
            s1 = 1
        elif term == '1 0':
            s2 = 1
        if (s1, s2) == (1, 1):
            break
    print('YES') if (s1, s2) == (1, 1) else print('NO')
elif k == 3:
    alert = 0
    s = {str(input()) for i in range(n)}
    if '0 0 0' in s:
        alert = 1
    if '0 0 1' in s:
        if '1 1 0' in s or '1 0 0' in s or '0 1 0' in s:
            alert = 1
    if '0 1 0' in s:
        if '1 0 1' in s or '1 0 0' in s or '0 0 1' in s:
            alert = 1
    if '1 0 0' in s:
        if '0 0 1' in s or '0 1 0' in s or '0 1 1' in s:
            alert = 1
    print('YES') if alert == 1 else print('NO')
elif k == 4:
    alert = 0
    s = {str(input()) for i in range(n)}
    s = list(s)
    if '0 0 0 0' in s:
        alert = 1
    if '1 1 0 0' in s:
        for i in range(len(s)):
            if s[i][0] == '0' and s[i][2] == '0':
                alert = 1
    if '1 0 1 0' in s:
        for i in range(len(s)):
            if s[i][0] == '0' and s[i][4] == '0':
                alert = 1
    if '1 0 0 1' in s:
        for i in range(len(s)):
            if s[i][0] == '0' and s[i][6] == '0':
                alert = 1
    if '0 1 1 0' in s:
        for i in range(len(s)):
            if s[i][2] == '0' and s[i][4] == '0':
                alert = 1
    if '0 1 0 1' in s:
        for i in range(len(s)):
            if s[i][2] == '0' and s[i][6] == '0':
                alert = 1
    if '0 0 1 1' in s:
        for i in range(len(s)):
            if s[i][4] == '0' and s[i][6] == '0':
                alert = 1
    if '1 0 0 0' in s:
        for i in range(len(s)):
            if s[i][0] == '0':
                alert = 1
    if '0 1 0 0' in s:
        for i in range(len(s)):
            if s[i][2] == '0':
                alert = 1
    if '0 0 1 0' in s:
        for i in range(len(s)):
            if s[i][4] == '0':
                alert = 1
    if '0 0 0 1' in s:
        for i in range(len(s)):
            if s[i][6] == '0':
                alert = 1
    print('YES') if alert == 1 else print('NO')
