from collections import Counter
N = int(input())
A = Counter(list(map(int, input().split())))
B = dict(sorted(list(A.items()), reverse=True))
ans = []
for i, j in list(B.items()):
    if j >= 4:
        ans.append(i)
        ans.append(i)
    if j >= 2:
        ans.append(i)
if len(ans) >= 2:
    print((ans[0] * ans[1]))
else:
    print((0))
