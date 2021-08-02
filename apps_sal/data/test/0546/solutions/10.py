good = input()
s = input()
pos = -1
for j in range(len(s)):
    if s[j] == '*':
        pos = j
        break
n = int(input())
hasStar = ('*' in s)
for i in range(n):
    t = input()
    if len(t) < len(s) - 1:
        print('NO')
        continue
    if hasStar:
        flag = True
        if len(t) <= (pos + 1) - 2:
            print('NO')
            continue
        if len(t) == (pos + 1) - 1:
            if len(s) >= (pos + 1) + 1:
                print('NO')
                continue

        for j in range(pos):
            if (t[j] not in good and s[j] == '?') or (s[j] != '?' and s[j] != t[j]):
                flag = False
                break
        if not flag:
            print('NO')
            continue
        l = pos
        r0 = len(t) - (len(s) - pos - 1)
        r = r0
        for j in range(pos + 1, len(s)):
            if (t[r] not in good and s[j] == '?') or (s[j] != '?' and s[j] != t[r]):
                flag = False
                break
            r += 1
        if not flag:
            print('NO')
            continue
        for j in range(l, r0):
            if t[j] in good:
                flag = False
                break
        if not flag:
            print('NO')
            continue
        print('YES')
    else:
        if len(s) != len(t):
            print('NO')
            continue
        flag = True
        for j in range(len(t)):
            if (t[j] not in good and s[j] == '?') or (s[j] != '?' and s[j] != t[j]):
                flag = False
                break
        if not flag:
            print('NO')
            continue
        print('YES')
