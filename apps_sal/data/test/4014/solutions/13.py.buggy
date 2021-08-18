#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n, m = rint()

s = [0 for i in range(m)]
d = [0 for i in range(m)]
c = [0 for i in range(m)]


for i in range(m):
    s[i], d[i], c[i] = rint()

s_in_day = [set() for i in range(n + 1)]
for i in range(m):
    day = s[i]
    s_in_day[day].add(i)

d_in_day = [-1 for i in range(n + 1)]
for i in range(m):
    day = d[i]
    d_in_day[day] = i


di_sorted = [0 for i in range(m)]
di_sorted.sort(key=lambda x: d[i])

ans = [0 for i in range(n + 1)]

candi_exam = set()
for day in range(1, n + 1):
    for exam in s_in_day[day]:
        candi_exam.add(exam)
    if d_in_day[day] != -1:
        exam = d_in_day[day]
        if c[exam] != 0:
            print(-1)
            return
        ans[day] = m + 1
        if exam in candi_exam:
            candi_exam.remove(exam)
        continue

    if len(candi_exam) == 0:
        ans[day] = 0
        continue
    min_d_day = 101
    busy_exam = 0
    for exam in candi_exam:
        if d[exam] < min_d_day:
            busy_exam = exam
            min_d_day = d[exam]

    ans[day] = busy_exam + 1
    c[busy_exam] -= 1
    if c[busy_exam] == 0:
        candi_exam.remove(busy_exam)
for i in range(m):
    if c[i] != 0:
        print(-1)
        return
print(*ans[1:])
