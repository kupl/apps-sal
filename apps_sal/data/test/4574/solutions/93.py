from collections import Counter

input()
ans = []
for i, j in list(Counter(list(map(int, input().split()))).items()):
    if j >= 4:
        ans.append(i)
    if j >= 2:
        ans.append(i)
if len(ans) >= 2:
    ans.sort()
    print((ans[-1] * ans[-2]))
else:
    print((0))

