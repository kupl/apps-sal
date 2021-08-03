import sys
n, k = map(int, input().split())
bothlike = []
alike = []
blike = []
for i in range(n):
    t, a, b = map(int, input().split())
    if a == 1 and b == 1:
        bothlike.append(t)
    if a == 1 and b == 0:
        alike.append(t)
    if a == 0 and b == 1:
        blike.append(t)
if len(alike) + len(bothlike) < k or len(blike) + len(bothlike) < k:
    print(-1)
    return
alike.sort()
blike.sort()
bothlike.sort()
asum = [0]
current = 0
for i in range(len(alike)):
    current += alike[i]
    asum.append(current)
bsum = [0]
current = 0
for i in range(len(blike)):
    current += blike[i]
    bsum.append(current)
bothcurrent = 0
ans = 10**18
alen = len(alike)
blen = len(blike)
bothlen = len(bothlike)
for i in range(bothlen + 1):
    if i > 0:
        bothcurrent += bothlike[i - 1]
    if i > k:
        break

    if k - i > alen or k - i > blen:
        continue
    ans = min(ans, asum[k - i] + bsum[k - i] + bothcurrent)
print(ans)
