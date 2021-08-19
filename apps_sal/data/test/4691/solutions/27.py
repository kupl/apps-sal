import collections
n = int(input())
list = []
for i in range(n):
    x = input()
    list.append(x)
c = collections.Counter(list)
print('AC x {}'.format(c['AC']))
print('WA x {}'.format(c['WA']))
print('TLE x {}'.format(c['TLE']))
print('RE x {}'.format(c['RE']))
