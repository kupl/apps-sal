import sys
# from io import StringIO
# sys.stdin = StringIO(open(__file__.replace('.py', '.in')).read())

s = list(input())

if len(s) < 26:
    print(-1)
    return

al = list('abcdefghijklmnopqrstuvwxyz')
i = 0
for j in range(len(s)):
    c = s[j]
    if ord(c) <= ord(al[i]):
        s[j] = al[i]
        i += 1
        if i == 26:
            break

if i >= 26:
    print(''.join(s))
else:
    print(-1)
