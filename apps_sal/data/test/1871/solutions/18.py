from sys import stdin as cin, stdout as cout
from math import factorial as f
from itertools import combinations as comb
(n, x) = list(map(int, cin.readline().split()))
a = list(map(int, cin.readline().split()))
a.sort()
t = 0
for i in range(n):
    m = x - i
    if m < 1:
        m = 1
    t += m * a[i]
print(t)
