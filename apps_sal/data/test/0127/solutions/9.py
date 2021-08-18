
from collections import namedtuple

n, f = (int(i) for i in input().split())

Day = namedtuple('Day', ('cur', 'diff'))

a = []

for i in range(n):
    k, l = (int(j) for j in input().split())
    a.append(Day((min(k, l)), min(2 * k, l) - min(k, l)))

a.sort(key=lambda day: day.diff, reverse=True)

print(sum(day.diff for day in a[:f]) + sum(day.cur for day in a))
