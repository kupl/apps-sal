import sys
from collections import Counter
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    if N % 2 == 1:
        print('Second')
        continue
    c = Counter(A)
    if max((v % 2 for v in list(c.values()))) == 0:
        print('Second')
    else:
        print('First')
