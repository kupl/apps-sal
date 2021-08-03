import sys
import math
import collections
import itertools
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
pa = []
cnt = 0
for i in range(N):
    if i + 1 == p[i]:
        cnt += 1
    elif i + 1 != p[i] and cnt > 0:
        pa.append(cnt)
        cnt = 0
if cnt > 0:
    pa.append(cnt)
cnt = 0
for cn in pa:
    cnt += cn // 2 + cn % 2
print(cnt)
