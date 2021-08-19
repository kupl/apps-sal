n = int(input())
s = list(input())


def findbal(a, th=0):
    b = 0
    for c in a:
        if c == '(':
            b += 1
        elif c == ')':
            b -= 1
            if th > 0 and b < th:
                return b
    return b


can = s[0] != ')' and s[-1] != '(' and (n % 2 == 0)
if can:
    s[0] = '('
    s[-1] = ')'
    b = findbal(s)
    q = sum([1 if c == '?' else 0 for c in s])
    q -= b
    q = q // 2
    if q < 0:
        can = False
    for i in range(n):
        if s[i] == '?':
            s[i] = '(' if q > 0 else ')'
            q -= 1
    can = findbal(s[:-1], 1) == 1
if can:
    print(''.join(s))
else:
    print(':(')
