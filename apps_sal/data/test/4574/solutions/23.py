import collections
N = int(input())
lsA = list(map(int, input().split()))
counterA = collections.Counter(lsA)
lsline = []
for i in counterA.keys():
    if counterA[i] >= 2:
        lsline.append(i)
lsline.sort(reverse=True)
if bool(lsline):
    if counterA[lsline[0]] >= 4:
        ans = lsline[0] * lsline[0]
    elif len(lsline) < 2:
        ans = 0
    else:
        ans = lsline[0] * lsline[1]
else:
    ans = 0
print(ans)
