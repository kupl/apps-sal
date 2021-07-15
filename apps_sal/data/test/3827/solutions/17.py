from collections import Counter

s = list(input().strip())
if s != sorted(s):
    print('NO')
    return
if set(s) != set(['a', 'b', 'c']):
    print('NO')
    return

x = Counter(s)
if x['c'] == x['a'] or x['c'] == x['b']:
    print('YES')
else:
    print('NO')

