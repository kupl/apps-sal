#!/usr/bin/env python3
cnt = [0] * 100002
input()
for x in map(int, input().split()):
    cnt[x] += 1
    cnt[x + 1] += 1
    cnt[x + 2] += 1
print(max(cnt))
