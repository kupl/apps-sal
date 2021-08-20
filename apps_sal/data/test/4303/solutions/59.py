(n, k) = map(int, input().split())
x = list(map(int, input().split()))
(pos, nega) = ([], [])
for v in x:
    if v >= 0:
        pos.append(v)
    else:
        nega.append(-v)
nega.sort()
ans = 10 ** 9
if k <= len(pos):
    ans = min(ans, pos[k - 1])
if k <= len(nega):
    ans = min(ans, nega[k - 1])
for i in range(k):
    if i < len(pos) and 0 <= k - i - 2 < len(nega):
        ans = min(ans, 2 * pos[i] + nega[k - i - 2])
    if i < len(nega) and 0 <= k - i - 2 < len(pos):
        ans = min(ans, 2 * nega[i] + pos[k - i - 2])
print(ans)
