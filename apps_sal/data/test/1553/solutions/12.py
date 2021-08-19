(n, h) = list(map(int, input().split()))
a = list(map(int, input().split()))


def check(k):
    if k == 0:
        return True
    ar = a[:k]
    ar = sorted(ar, key=lambda x: -x)
    s = 0
    for i in range((k + 1) // 2):
        m = ar[2 * i]
        s += m
    return s <= h


l = 0
r = len(a)
ans = 0
while r >= l:
    m = (r + l) // 2
    if check(m):
        ans = max(ans, m)
        l = m + 1
    else:
        r = m - 1
print(ans)
