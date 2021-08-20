import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = 10 ** 18
eps = 10 ** (-7)
kuku = range(1, 10)
n = int(input())
d = False
for i in kuku:
    if n % i == 0 and n // i < 10:
        d = True
if d:
    print('Yes')
else:
    print('No')
