from collections import Counter

input()
d = Counter(map(int, input().split()))
d = dict(sorted(d.items(), reverse=True))
ans = []
for i, j in d.items():
    if j >= 4:
        ans.append(i)
    if j >= 2:
        ans.append(i)
if len(ans) >= 2:
    print(ans[0] * ans[1])
else:
    print(0)
