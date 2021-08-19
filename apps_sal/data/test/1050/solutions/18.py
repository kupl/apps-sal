import math
import sys

# imgur.com/Pkt7iIf.png


def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


n, m, k = mi()
if min(m, k) >= n:
    print('Yes')
else:
    print('No')
