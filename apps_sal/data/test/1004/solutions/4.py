from collections import defaultdict
n = int(input())
l = [*map(int, input().split())]

valid = True
res = []

cnt = defaultdict(int)
cur = 0
for e in l:
    if e < 0:
        valid &= cnt[-e] == 1
        cnt[-e] += 1
        cur += 1
    else:
        valid &= cnt[e] == 0
        cnt[e] += 1
    if cur == len(cnt):
        res.append(2 * cur)
        cnt.clear()
        cur = 0

    if not valid: break
valid &= cur == 0 and not cnt
if not valid:
    print(-1)
else:
    print(len(res))
    print(*res)
