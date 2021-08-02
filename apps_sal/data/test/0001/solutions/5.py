import sys


def calc(s):
    res = 0
    for c in s:
        res += int(c)
    return res


s = list(sys.stdin.readline().rstrip())
best = "".join(s)
count = calc(s)

i = len(s) - 1
while i != 0:
    i -= 1
    if s[i + 1] != '9':
        s[i + 1] = '9'
        while s[i] == '0':
            s[i] = '9'
            i -= 1
        s[i] = chr(ord(s[i]) - 1)
        c = calc(s)
        if count < c:
            count = c
            best = "".join(s)

if best[0] == '0':
    best = best[1:]

print(best)
