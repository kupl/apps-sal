from math import log, floor
n, I = list(map(int, input().split()))
a = [int(s) for s in input().split()]
b = []
a.sort()
b.append([-1, 0])
for i in range(0, n):
    if a[i] == b[-1][0]:
        b[-1][1] += 1
    else:
        b.append([a[i], b[-1][1] + 1])
maxk = I * 8 // n
maxK = 1 << maxk
# print(maxk, maxK)
ans = n
# print(b)
if len(b) - 1 < maxK:
    ans = 0
else:
    for i in range(len(b) - maxK):
        chg = n - (b[i + maxK][1] - b[i][1])
        if chg < ans:
            ans = chg
print(ans)
