input()
s = list(input())
r, d = map(s.count, ('R', 'D'))
rf, df = 0, 0

while r > 0 and d > 0:
    for i, v in enumerate(s):
        if v == 'D':
            if rf:
                rf -= 1
                d -= 1
                s[i] = ' '
            else:
                df += 1
        elif v == 'R':
            if df:
                df -= 1
                r -= 1
                s[i] = ' '
            else:
                rf += 1

print('D' if d else 'R')
