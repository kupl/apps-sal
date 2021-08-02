from collections import Counter as Cnt

s = input()

cur = 0
while cur < len(s) and s[cur] == 'a':
    cur += 1

if cur == len(s):
    print('NO')
    return

while cur < len(s) and s[cur] == 'b':
    cur += 1

while cur < len(s) and s[cur] == 'c':
    cur += 1

if cur != len(s):
    print('NO')
    return

c = Cnt(s)
if c['a'] > 0 and c['b'] > 0 and (c['c'] == c['a'] or c['c'] == c['b']):
    print('YES')
else:
    print('NO')
