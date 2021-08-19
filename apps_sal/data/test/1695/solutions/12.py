# 577_A

import sys

ln = [int(i) for i in input().split(" ")]

n = ln[0]
m = ln[1]

ans = []

for i in range(0, n):
    ans.append(list(sys.stdin.readline().rstrip()))

arr = ["A", "B", "C", "D", "E"]

pts = [int(i) for i in input().split(" ")]

s = 0

for i in range(0, m):
    cts = [0, 0, 0, 0, 0]
    for j in range(0, n):
        cts[arr.index(ans[j][i])] += 1
    s += max(cts) * pts[i]

print(s)
