n = int(input())
s = list(input())
d = {i: 0 for i in '012'}
for i in s:
    d[i] += 1
eq = n // 3
i = 0
while d['0'] < eq:
    if s[i] != '0':
        if d[s[i]] > eq:
            d[s[i]] -= 1
            d['0'] += 1
            s[i] = '0'
    i += 1
i = n - 1
while d['2'] < eq:
    if s[i] != '2':
        if d[s[i]] > eq:
            d[s[i]] -= 1
            d['2'] += 1
            s[i] = '2'
    i -= 1
i = n - 1
while d['1'] < eq and i >= 0:
    if s[i] == '0':
        if d[s[i]] > eq:
            d[s[i]] -= 1
            d['1'] += 1
            s[i] = '1'
    i -= 1
i = 0
while d['1'] < eq and i < n:
    if s[i] == '2':
        if d[s[i]] > eq:
            d[s[i]] -= 1
            d['1'] += 1
            s[i] = '1'
    i += 1
print(*s, sep='')
