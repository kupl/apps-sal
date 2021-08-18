'''input
4
5
11
1
3
'''
from sys import stdin, stdout


from collections import defaultdict, deque

t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline().strip())
    ans = set()
    for i in range(1, int(n ** 0.5) + 1):
        ans.add(i)
        ans.add(n // i)

    ans.add(0)
    ans.add(1)
    ans.add(n)
    ans = list(ans)
    ans.sort()
    print(len(ans))
    print(*ans)
