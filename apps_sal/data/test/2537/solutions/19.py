q = int(input())
for _ in range(q):
    s = list(input())
    t = list(input())
    p = list(input())
    i = 0
    j = 0
    u = True
    while i < len(s):
        while j < len(t):
            if t[j] == s[i]:
                t[j] = ''
                j += 1
                break
            j += 1
        i += 1
    if t.count('') != len(s):
        print('NO')
        continue
    for i in p:
        for j in range(len(t)):
            if t[j] == i:
                t[j] = ''
                break
    t = ''.join(t)
    if t == '':
        print('YES')
    else:
        print('NO')
