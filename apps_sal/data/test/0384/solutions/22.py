def getin():
    xin = input()
    while xin.strip() == '':
        xin = input()
    return xin


def gi():
    return [int(x) for x in getin().split()]


input()
s = input()
ch = s[0]
i = 1
cur = 1 if ch == 'B' else 0
ans = []
while i < len(s):
    if s[i] == 'B':
        if ch == 'B':
            cur += 1
        else:
            cur = 1
    elif s[i] == 'W':
        if ch == 'B':
            ans.append(cur)
        cur = 0
    ch = s[i]
    i += 1
if cur > 0:
    ans.append(cur)
print(len(ans))
if len(ans) > 0:
    print(' '.join([str(x) for x in ans]))
