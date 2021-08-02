from sys import stdin
from collections import defaultdict
input = stdin.readline
# ~ T = int(input())
T = 1
for t in range(1, T + 1):
    n, k = list(map(int, input().split()))
    _input = []
    for i in range(n):
        _input.append(int(input()))
    _input.sort()
    min_ans = 10000000000
    for i in range(k - 1, len(_input)):
        min_ans = min(min_ans, _input[i] - _input[i - k + 1])
    print(min_ans)
