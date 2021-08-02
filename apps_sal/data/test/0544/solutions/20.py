t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    for i in range(n):
        s[i] = ord(s[i]) - 97
    ok = True
    for i in range(n // 2):
        if s[i] == s[-i - 1]:
            continue
        if s[i] == s[-i - 1] - 2 and s[-i - 1] > 1:
            continue
        if s[i] == s[-i - 1] + 2:
            continue
        print('NO')
        ok = False
        break
    if ok:
        print('YES')
