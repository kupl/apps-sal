#-*-coding:utf-8 -*-
from collections import defaultdict

n, m = map(int, input().split())
s = input()

mp = defaultdict(int)

for i in s:
    mp[i] += 1

cnt = defaultdict(int)

mk = 'abcdefghijklmnopqrstuvwxyz'

for i in mk:
    if mp[i] == 0:
        continue

    cnt[i] += min(m, mp[i])
    m -= min(m, mp[i])

    if m == 0:
        break

for i in s:
    if cnt[i] > 0:
        cnt[i] -= 1
    else:
        print(i, end='')








