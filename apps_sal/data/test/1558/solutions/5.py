__author__ = 'valeriy.shevchuk'
from math import ceil
(n, r, avg) = map(int, input().split())
data = []
sum_v = 0
for i in range(n):
    (a, b) = map(int, input().split())
    sum_v += a
    data.append((a, b))
need = ceil(max(avg * n - sum_v, 0))
data = sorted(data, key=lambda x: x[1])
ref = 0
for i in range(len(data)):
    if need <= 0:
        break
    if data[i][0] < r:
        grades = min(r - data[i][0], need)
        ref += grades * data[i][1]
        need -= grades
print(ref)
