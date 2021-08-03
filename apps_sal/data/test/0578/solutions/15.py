inp = input()
a, inp = inp.split('.')
d, b = inp.split('e')
b = int(b)

whole = a + d

ans = ''
if b >= len(d):
    ans = d + '0' * (b - len(d))

    if a != '0':
        ans = a + ans
else:
    #ans = a + d[:b] + '.' + d[b:]

    ans = a + d[:b]
    if (len(ans) > 1) and (ans[0] == '0'):
        ans = d[:b]

    if d[b:] != '0':
        ans += '.' + d[b:]


print(ans)
