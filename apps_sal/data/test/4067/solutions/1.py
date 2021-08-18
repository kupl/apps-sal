n = int(input())

s = list(input())

c = {c: s.count(c) for c in '012'}

i = 0

while c['0'] < n // 3 and i < n:
    if s[i] != '0' and c[s[i]] > n // 3:
        c[s[i]] -= 1
        c['0'] += 1
        s[i] = '0'

    i += 1

i = 0

while c['1'] < n // 3 and i < n:
    if s[i] == '2' and c[s[i]] > n // 3:
        c[s[i]] -= 1
        c['1'] += 1
        s[i] = '1'

    i += 1

i = n - 1

while c['2'] < n // 3 and i > 0:
    if s[i] != '2' and c[s[i]] > n // 3:
        c[s[i]] -= 1
        c['2'] += 1
        s[i] = '2'

    i -= 1

i = n - 1

while c['1'] < n // 3 and i > 0:
    if s[i] != '1' and c[s[i]] > n // 3:
        c[s[i]] -= 1
        c['1'] += 1
        s[i] = '1'

    i -= 1

print(''.join(s))
