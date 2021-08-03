__author__ = 'tanunia'

from sys import stdin

n, m = [int(k) for k in stdin.readline().split()]
lst = []
for _ in range(n):
    s, r = [int(k) for k in stdin.readline().split()]
    lst.append([s - 1, r])

lst = sorted(lst, key=lambda x: -x[1])

students_num = [[0, 0] for _ in range(m)]
best_score = [0 for _ in range(n + 1)]
for it in lst:
    sub, rating = it[0], it[1]
    students_num[sub][0] += rating
    students_num[sub][1] += 1
    if students_num[sub][0] > 0:
        best_score[students_num[sub][1]] += students_num[sub][0]

print(max(best_score))
