import sys
from math import floor, ceil

input = sys.stdin.readline

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

totBad = 0
totGood = 0

for i in a:
    if i == -1:
        totBad += 1
    else:
        totGood += 1

ans = 0
for i in range(k):
    curBad = 0
    curGood = 0
    for j in range(i, n, k):
        if a[j] == -1:
            curBad += 1
        else:
            curGood += 1
    ans = max(ans, abs((totBad - curBad) - (totGood - curGood)))

print(ans)
