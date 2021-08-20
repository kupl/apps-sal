import math
from collections import deque
from collections import defaultdict
t = int(input())
while t > 0:
    t -= 1
    (n, x) = list(map(int, input().strip().split(' ')))
    if n == 1 or n == 2:
        print(1)
    else:
        n -= 2
        print(math.ceil(n / x) + 1)
