from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
pos = 0
neg = 0
z = 0
ans = 0
for x in l:
    if x > 0:
        pos += 1
        ans += x - 1
    elif x < 0:
        neg += 1
        ans += -1 - x
    else:
        z += 1
        ans += 1
if neg % 2 == 0:
    print(ans)
elif z > 0:
    print(ans)
else:
    print(ans + 2)
