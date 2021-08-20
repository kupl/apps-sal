from math import ceil
from sys import stdin
n = int(stdin.readline().strip())
s = list(map(int, stdin.readline().strip().split()))
s1 = s[::-1]
d = n - 1
mn = 10 ** 20
k = 10 ** 20
while d >= n // 2:
    mn = min(s1[-1], s[-1], mn)
    s1.pop()
    s.pop()
    k = min(k, mn // d)
    d -= 1
print(k)
