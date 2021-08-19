n = int(input())
(l, r) = (-1000000001, 1000000001)
for i in range(n):
    s = input().split()
    if s[2] == 'Y':
        if s[0] == '>':
            l = max(l, int(s[1]) + 1)
        elif s[0] == '>=':
            l = max(l, int(s[1]))
        elif s[0] == '<':
            r = min(r, int(s[1]) - 1)
        else:
            r = min(r, int(s[1]))
    elif s[0] == '<=':
        l = max(l, int(s[1]) + 1)
    elif s[0] == '<':
        l = max(l, int(s[1]))
    elif s[0] == '>=':
        r = min(r, int(s[1]) - 1)
    else:
        r = min(r, int(s[1]))
if r < l:
    print('Impossible')
elif r == 1000000001 and l == -1000000001:
    print(1)
elif r == 1000000001:
    print(l)
elif l == -1000000001:
    print(r)
else:
    print(r)
