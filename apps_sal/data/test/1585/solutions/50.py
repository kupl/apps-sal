import sys
import pprint
import math
import itertools
from collections import defaultdict
input = sys.stdin.readline

X, Y = list(map(int, input().split()))
ans = 0
for i in range(X, X + 100):
    now = i
    cnt = 0
    while True:
        if now <= Y:
            cnt += 1
            now *= 2
        else:
            break
    ans = max(ans, cnt)
print(ans)
