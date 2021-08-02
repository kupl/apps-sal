from sys import stdin
from bisect import bisect_left as bl
input = stdin.readline
n = int(input())
a = []
b = []
for i in range(n):
    c, d = map(int, input().split())
    if c < d:
        a.append([d, i])
    else:
        b.append([c, i])
a.sort(reverse=True)
b.sort()
if len(a) > len(b):
    print(len(a))
    for i in a:
        print(i[1] + 1, end=' ')
else:
    print(len(b))
    for i in b:
        print(i[1] + 1, end=' ')
