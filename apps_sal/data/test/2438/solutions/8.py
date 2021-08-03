import sys
import math
from collections import defaultdict
from itertools import combinations
from itertools import permutations
def input(): return sys.stdin.readline().rstrip()
def read(): return list(map(int, input().split()))


def write(*args, sep="\n"):
    for i in args:
        sys.stdout.write("{}".format(i) + sep)


INF = float('inf')
MOD = int(1e9 + 7)

n = int(input())
s = input()
arr = [[s[0], 1]]

for i in s[1:]:
    if i == arr[-1][0]:
        arr[-1][1] += 1
    else:
        arr.append([i, 1])

ans = (n) * (n - 1) // 2

if len(arr) == 1:
    print(ans)
    return

elif len(arr) == 2:
    ans -= arr[0][1]
    ans -= arr[1][1]
    print(ans + 1)
    return

else:
    # print(arr)
    ans -= arr[1][1]
    ans -= arr[-2][1]
    for i in range(1, len(arr) - 1):
        ans -= arr[i - 1][1]
        ans -= arr[i + 1][1]
        ans += 1
    print(ans + 1)
