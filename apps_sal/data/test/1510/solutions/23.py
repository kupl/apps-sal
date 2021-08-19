from sys import stdin
(n, m) = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
l = min(min(a), min(b))
r = max(max(a), max(b))
ans = 10 ** 20
while l <= r:
    lo = l + (r - l) // 3
    hi = r - (r - l) // 3
    cou = 0
    for i in a:
        cou += max(0, lo - i)
    for j in b:
        cou += max(0, j - lo)
    cou1 = 0
    for i in a:
        cou1 += max(0, hi - i)
    for j in b:
        cou1 += max(0, j - hi)
    if cou1 > cou:
        r = hi - 1
    elif cou1 < cou:
        l = lo + 1
    else:
        l = lo + 1
        r = hi - 1
    ans = min(ans, cou, cou1)
print(ans)
