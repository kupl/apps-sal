import sys
import math
from collections import defaultdict
from itertools import combinations
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()
read = lambda: map(int, input().split())


def write(*args, sep="\n"):
    for i in args:
        sys.stdout.write("{}".format(i) + sep)


INF = float('inf')
MOD = int(1e9 + 7)

for _ in range(int(input())):
    s = input()
    ans = ""
    for i in sorted(set(s)):
        if (not (i + i) in s) or (s.count(i + i) * 2 - s.count(i) < 0):
            ans += i

    print(ans)
