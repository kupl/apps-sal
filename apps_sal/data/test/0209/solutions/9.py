from sys import stdin as cin
from fractions import gcd
mod = 1000000007
(x, y) = list(map(int, cin.readline().split()))
n = int(cin.readline())
k = n % 6
if k == 0:
    print((x - y) % mod)
elif k == 1:
    print(x % mod)
elif k == 2:
    print(y % mod)
elif k == 3:
    print((y - x) % mod)
elif k == 4:
    print(-x % mod)
elif k == 5:
    print(-y % mod)
