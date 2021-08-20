from math import sqrt, floor
from collections import defaultdict
n = int(input())
p = list(map(int, input().split()))
dic = defaultdict(int)
for i in range(n):
    dic[i + 1] = p[i]
ans = [0]
for i in range(1, n + 1):
    dic_ = defaultdict(int)
    dic_[i] += 1
    tmp = dic_[i]
    cur = i
    while tmp != 2:
        cur = dic[cur]
        dic_[cur] += 1
        tmp = dic_[cur]
    print(cur, end=' ')
