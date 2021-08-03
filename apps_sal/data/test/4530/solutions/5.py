'''
4
7
4 2 4 1 4 3 4
5
2 1 5 4 3
1
1
4
1 1 1 3
'''
from collections import Counter as c
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    t = c(a)
    l = [[t[a], a] for a in t]
    l.sort(reverse=True)
    b = l[0][0]
    a = len(l) - 1
    print(max(min(a, b), min(a + 1, b - 1)))
