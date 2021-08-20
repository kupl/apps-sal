from collections import Counter
n = int(input())
s = list(input())
c = Counter(s[:-10])
if c['8'] > len(s[:-10]) // 2:
    print('YES')
else:
    print('NO')
