import sys
import math
from collections import defaultdict
from collections import deque
from itertools import combinations
from itertools import permutations
def input(): return sys.stdin.readline().rstrip()
def read(): return list(map(int, input().split()))
def go(): return 1 / 0


def write(*args, sep="\n"):
    for i in args:
        sys.stdout.write("{}{}".format(i, sep))


INF = float('inf')
MOD = int(1e9 + 7)
YES = "YES"
NO = "NO"


def f(x):
    return bin(x)[2:][::-1]


n = int(input())
cnt = [0] * 100
arr = read()

for i in arr:
    s = f(i)

    for j in range(len(s)):
        if s[j] == "1":
            cnt[j] += 1

ans = [-INF, -INF]
for i in arr:
    s = f(i)

    for j in range(len(s)):
        if s[j] == "1":
            cnt[j] -= 1

    x = []
    for j in range(len(s)):
        if cnt[j] == 0:
            x.append(s[j])
        else:
            x.append("0")

    ans = max(ans, [int("".join(x)[::-1], 2), i])

    for j in range(len(s)):
        if s[j] == "1":
            cnt[j] += 1

arr.remove(ans[1])

print(ans[1], *arr)
