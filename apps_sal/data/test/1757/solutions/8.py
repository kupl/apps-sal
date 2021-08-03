from collections import defaultdict
from collections import deque
from collections import Counter
import sys
sys.setrecursionlimit(1000000)


def fib():
    ls = [1, 1]
    for i in range(100):
        ls.append(ls[-1] + ls[-2])
    return set(ls)


n = int(input())
s = []
f = fib()
for i in range(1, n + 1):
    if i in f:
        s.append('O')
    else:
        s.append('o')
print(''.join(s))
