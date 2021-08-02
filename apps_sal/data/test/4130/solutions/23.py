import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
d = defaultdict(int)

for i in arr:
    d[i] += 1
    if d[i] == 4:
        d[i] = 3

cnt = [0] * 150009

for i, j in sorted(d.items()):
    if j == 3:
        if i - 1 > 0:
            cnt[i - 1] = 1
        cnt[i] = 1
        cnt[i + 1] = 1

    elif j == 1:
        #print(cnt[i-1], cnt[i], cnt[i+1])
        if i - 1 > 0 and cnt[i - 1] == 0:
            cnt[i - 1] = 1
            continue
        if cnt[i] == 0:
            cnt[i] = 1
            continue
        if cnt[i + 1] == 0:
            cnt[i + 1] = 1
            continue

    else:
        cnt2 = 0
        if i - 1 > 0 and cnt[i - 1] == 0:
            cnt[i - 1] = 1
            cnt2 += 1
        if cnt[i] == 0:
            cnt[i] = 1
            cnt2 += 1
        if cnt2 == 2:
            continue

        if cnt[i + 1] == 0:
            cnt[i + 1] = 1
            continue

print(sum(cnt))
