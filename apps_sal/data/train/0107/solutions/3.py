from sys import stdin, stdout
from collections import defaultdict
input = stdin.readline
for _ in range(int(input())):
    (a, b, c, d) = map(int, input().split())
    (small, large, positive) = (0, 0, 1)
    if a > 0 or d > 0:
        large = 1
    if b > 0 or c > 0:
        small = 1
    if (a + b) % 2:
        positive = 0
    l = list()
    if large and (not positive):
        l.append('Ya')
    else:
        l.append('Tidak')
    if small and (not positive):
        l.append('Ya')
    else:
        l.append('Tidak')
    if small and positive:
        l.append('Ya')
    else:
        l.append('Tidak')
    if large and positive:
        l.append('Ya')
    else:
        l.append('Tidak')
    print(*l)
