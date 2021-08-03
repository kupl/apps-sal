import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()


n = int(input(), 2)

ans = 0

i = 0
while 4**i < n:
    ans += 1
    i += 1

print(ans)
