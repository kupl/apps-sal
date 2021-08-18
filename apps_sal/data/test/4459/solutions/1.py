from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
ans = 0

dd = defaultdict(int)
for key in a:
    dd[key] += 1
for key in dd.keys():
    if dd[key] >= key:
        ans += dd[key] - key
    else:
        ans += dd[key]
print(ans)
