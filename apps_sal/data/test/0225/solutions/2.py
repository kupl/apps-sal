import sys
from collections import defaultdict
from itertools import combinations
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()


def write(*args, sep=" "):
    for i in args:
        sys.stdout.write("{}".format(i) + sep)


INF = float('inf')
MOD = int(1e9 + 7)

arr = list(map(int, input().split()))
s = sum(arr)
for i in range(1, 5):
    for j in combinations(arr, i):
        # print(j)
        if sum(j) == s - sum(j):
            print("YES")
            return

print("NO")
