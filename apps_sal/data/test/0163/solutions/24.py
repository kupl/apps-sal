(n, k) = list(map(int, input().split()))
s = input()
(g, t) = (0, 0)
for i in range(len(s)):
    if s[i] == 'G':
        g = i
    if s[i] == 'T':
        t = i
if (t - g) % k == 0:
    if t > g:
        i = g
        B = True
        while i < t:
            if s[i] == '#':
                B = False
                break
            i += k
    else:
        i = t
        B = True
        while i < g:
            if s[i] == '#':
                B = False
                break
            i += k
    if B:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
