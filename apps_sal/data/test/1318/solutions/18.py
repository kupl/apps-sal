from collections import namedtuple
n = int(input())
Table = namedtuple('Table', 'id, size')
Group = namedtuple('Group', 'id, size, income')


def first_fit(size):
    for t in tables:
        if t.size >= size and t.id not in used_tables:
            used_tables.add(t.id)
            return t


(tables, groups) = ([], [])
used_tables = set()
for i in range(n):
    (c, p) = list(map(int, input().split()))
    groups.append(Group(i + 1, c, p))
k = int(input())
r = list(map(int, input().split()))
for i in range(k):
    tables.append(Table(i + 1, r[i]))
groups.sort(key=lambda group: group.income, reverse=True)
tables.sort(key=lambda table: table.size)
sum_ = 0
ans = []
for i in range(n):
    g = groups[i]
    needed_table = first_fit(g.size)
    if not needed_table:
        continue
    sum_ += g.income
    ans.append((g.id, needed_table.id))
print(len(ans), sum_)
for a in ans:
    print(*a)
