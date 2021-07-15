from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
d = defaultdict(int)
for x in A:
    d[x] += 1
cnt = 0
for x in d:
    if d[x] >= 2 and d[x] % 2 == 0:
        cnt += 1
ans = len(d.keys())
if cnt % 2 == 1:
    ans -= 1
print(ans)
