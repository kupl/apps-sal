def f(t):
    if t == '':
        return 0
    m = len(t)
    if '.' not in t:
        return int(t) * 100
    if t[-3] != '.':
        t += '00'
    t2 = ''.join([i for i in t if i != '.'])
    return int(t2)


def wr(x):
    if x < 100:
        res = '0.'
        if x < 10:
            res += '0'
        res += str(x)
        return res
    x = str(x)
    m = len(x)
    res = x[-2:]
    for i in range(m - 2, 2, -3):
        res = x[i - 3:i] + '.' + res
    res = x[0:(m - 2) % 3] + '.' + res
    if res[0] == '.':
        res = res[1:]
    if res[-2:] == '00':
        res = res[:-3]
    return res


s = input() + '_'
num = '1234567890.'
ans = 0
n = len(s)
cur = ''
for i in range(n):
    if s[i] not in num:
        ans += f(cur)
        cur = ''
    else:
        cur += s[i]
print(wr(ans))
