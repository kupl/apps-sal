(n, p) = map(int, input().split())
s = input()
d = s.count('d')
u = s.count('u')
if d <= p or u <= p:
    print(n)
elif d >= u:
    c = 0
    l = 0
    i = 0
    ii = -1
    pp = p
    while i < n:
        if s[i] == 'u' and ii == -1:
            ii = i
        if pp == 0 and s[i] == 'u':
            c = max(c, l)
            i = ii
            ii = -1
            l = -1
            pp = p
        elif s[i] == 'u':
            pp -= 1
        i += 1
        l += 1
    print(max(c, l))
else:
    c = 0
    l = 0
    i = 0
    ii = -1
    pp = p
    while i < n:
        if s[i] == 'd' and ii == -1:
            ii = i
        if pp == 0 and s[i] == 'd':
            c = max(c, l)
            i = ii
            ii = -1
            l = -1
            pp = p
        elif s[i] == 'd':
            pp -= 1
        i += 1
        l += 1
    print(max(c, l))
