s = input()
l = len(s)
(a, b, d) = (-1, -1, -1)
ae = 0
for i in range(l):
    if s[i] == '.':
        a = s[:i]
        ae = i
    elif s[i] == 'e':
        b = s[ae + 1:i]
        d = int(s[i + 1:])
if len(b) <= d:
    ans = int(a + b + '0' * (d - len(b)))
    print(ans)
else:
    ans = a + b[:d]
    flag = True
    for c in b[d:]:
        if c != '0':
            flag = False
    if not flag:
        ans += '.' + b[d:]
    print(ans)
