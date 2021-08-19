from sys import stdin as cin
from fractions import gcd
mod = 1000000007
(n, m) = map(int, cin.readline().split())
if min(m, n) % 2 == 0:
    print('Malvika')
else:
    print('Akshat')
