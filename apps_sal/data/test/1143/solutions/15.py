from datetime import date, timedelta
import math
w = open('output.txt', 'w')
r = open('input.txt', 'r')
oplympiads = []
min_date = date(2014, 1, 1)
max_date = date(2011, 1, 1)
n = int(r.readline())
for _ in range(n):
    (m, d, p, t) = map(int, r.readline().split())
    oplympiads.append((m, d, p, t))
    if date(2013, m, d) > max_date:
        max_date = date(2013, m, d)
    if date(2013, m, d) - timedelta(t) < min_date:
        min_date = date(2013, m, d) - timedelta(t)
days_needed = (max_date - min_date).days
number_of_workers_in_day = [0] * days_needed
for (m, d, p, t) in oplympiads:
    for dte in range(t):
        number_of_workers_in_day[(date(2013, m, d) - timedelta(t - dte) - min_date).days] += p
w.write('{}'.format(max(number_of_workers_in_day)))
