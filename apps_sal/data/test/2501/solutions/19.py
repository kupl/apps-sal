#!/usr/bin/env python3
import collections
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# 2人の持つ番号の差の絶対値が、2人の身長の和に等しい。
# j - i = Ai + Aj
# j - Aj = Ai + i
l = [j - aj for j, aj in enumerate(a, 1)]
r = [i + ai for i, ai in enumerate(a, 1)]
cnt = collections.Counter(r)
ans = 0
for i in l:
    ans += cnt[i]
print(ans)
