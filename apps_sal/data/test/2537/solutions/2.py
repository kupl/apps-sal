from sys import stdin
c = int(stdin.readline().strip())
for cas in range(c):
    s = list(stdin.readline().strip())
    t = list(stdin.readline().strip())
    p = list(stdin.readline().strip())
    rem = 0
    flag = False
    x = s[0]
    y = 0
    for i in range(len(t)):
        if x == t[i]:
            y += 1
            if y == len(s):
                flag = True
                break
            x = s[y]

    for i in range(len(s)):
        if s[i] in t:
            t.remove(s[i])
            rem += 1
    for i in range(len(p)):
        if p[i] in t:
            t.remove(p[i])

    if len(t) == 0 and rem == len(s) and flag:
        print("YES")
    else:
        print("NO")
