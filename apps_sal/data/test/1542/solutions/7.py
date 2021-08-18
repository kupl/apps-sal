
from bisect import bisect

n = int(input())
x = sorted([int(x) for x in input().split()])
q = int(input())
for _ in range(q):
    m = int(input())
    print(bisect(x, m))
