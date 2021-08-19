s = input().split()
t = s[:]
req = int(s[-1])
lim = req
S = 0
for i in range(len(s)):
    if s[i] == '?':
        s[i] = '1'
        S += 1 if i == 0 or s[i - 1] == '+' else -1
if S < req:
    for i in range(len(s)):
        if t[i] == '?':
            sign = 1 if i == 0 or s[i - 1] == '+' else -1
            if sign == 1:
                d = min(req - S, lim - 1)
                s[i] = str(d + 1)
                S += d
else:
    for i in range(len(s)):
        if t[i] == '?':
            sign = 1 if i == 0 or s[i - 1] == '+' else -1
            if sign == -1:
                d = min(S - req, lim - 1)
                s[i] = str(d + 1)
                S -= d
if S == req:
    print('Possible')
    print(' '.join(s))
else:
    print('Impossible')
