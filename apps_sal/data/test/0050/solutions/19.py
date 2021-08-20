import sys
from itertools import accumulate
input = sys.stdin.readline


def ii():
    return int(input())


def mi():
    return list(map(int, input().rstrip().split()))


def lmi():
    return list(map(int, input().rstrip().split()))


def li():
    return list(input().rstrip())


(n, m, r) = mi()
s = lmi()
b = lmi()
s.sort()
b.sort()
b.reverse()
a = s[0]
z = b[0]
print(max(r + (z - a) * (r // a), r))
