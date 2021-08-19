import collections
n = int(input())
res = [input() for i in range(n)]
a = collections.Counter(res)
print('{} x {}'.format('AC', a['AC']))
print('{} x {}'.format('WA', a['WA']))
print('{} x {}'.format('TLE', a['TLE']))
print('{} x {}'.format('RE', a['RE']))
