from sys import stdin as cin
from fractions import gcd
mod = 1000000007
n, m, k = map(int,cin.readline().split())

if k>(n+m-2):
    print(-1)

else:
    if n < m:
        n,m = m,n
    max_min_area = max((n*(m//(k+1))),(m*(n//(k+1))))
    if (k+1) > m:
        max_min_area = max(max_min_area,n//(k-m+2))
    if (k+1) > n:
        max_min_area = max(max_min_area,m//(k-n+2))
    print(max_min_area)
