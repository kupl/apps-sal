import sys
from math import ceil, floor
input = sys.stdin.readline
n = int(input())
ans = [0 for i in range(n)]
a = list(map(int, input().split()))
for i in range(len(a)):
    ans[i] = 0
    ans[n - i - 1] = a[i]
for i in range(1, len(a)):
    back = n - i - 1
    if ans[i] < ans[i - 1]:
        diff = ans[i - 1] - ans[i]
        ans[i] += diff
        ans[back] -= diff
    while ans[back] > ans[back + 1]:
        diff = ans[back] - ans[back + 1]
        ans[i] += diff
        ans[back] -= diff
print(' '.join([str(x) for x in ans]))
